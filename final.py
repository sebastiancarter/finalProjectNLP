import streamlit as st
from ollama import Client
import json

def initialize_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "You will recieve a programming assignment that is either in progress or has been completed by an undergraduate CS student. Create an explanation of the key topics being covered in the assignment."
    if "custom_prompt_enabled" not in st.session_state:
        st.session_state.custom_prompt_enabled = False

def get_ollama_response(prompt, model="llama2"):
    client = Client(host='http://localhost:11434')
    
    try:
        response = client.chat(model=model, messages=[
            {
                'role': 'system',
                'content': st.session_state.system_prompt
            },
            {
                'role': 'user',
                'content': prompt
            }
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("💬 MEB-GPT Chat Interface")
    
    # Initialize chat history
    initialize_chat_history()
    
    # Sidebar for model selection
    with st.sidebar:
        st.header("Settings")
        model = st.selectbox(
            "Choose your model",
            ["MEB-GPT-BOTH", "MEB-GPT", "MEB-GPT-LECTURE", "llama3.2"],

            index=0
        )
        

        st.markdown("---")
        st.subheader("System Prompt")

        # Default system prompt
        default_prompt = "You will recieve a programming assignment that is either in progress or has been completed by an undergraduate CS student. Create an explanation of the key topics being covered in the assignment."

        # Checkbox for custom system prompt
        custom_prompt = st.checkbox("Use custom system prompt",
                                  value=st.session_state.custom_prompt_enabled)

        # If checkbox state changes
        if custom_prompt != st.session_state.custom_prompt_enabled:
            st.session_state.messages = []  # Clear chat history
            st.session_state.custom_prompt_enabled = custom_prompt
            if not custom_prompt:
                st.session_state.system_prompt = default_prompt

        # Text area for system prompt, only shown when checkbox is enabled
        if custom_prompt:
            new_system_prompt = st.text_area(
                "Enter custom system prompt:",
                value=st.session_state.system_prompt,
                height=150
            )
            if new_system_prompt != st.session_state.system_prompt:
                st.session_state.messages = []  # Clear chat history
                st.session_state.system_prompt = new_system_prompt
                st.success("System prompt updated and chat history cleared!")

        st.markdown("---")
        st.markdown("""
        ### About
        This is a chat interface for Ollama models.
        Make sure you have:
        1. Ollama installed
        2. The selected model installed using our model files
        3. Ollama running locally
        """)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Put your code here to see more info"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ollama_response(prompt, model)
                st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()



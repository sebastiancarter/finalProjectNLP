import requests
import json

with open("key.txt", 'r') as keyFile:
    key = keyFile.read()

key = key.strip()

with open("question.txt", 'r') as messageFile:
    message = messageFile.read()

message = message.strip()
messageJson = {"messages":[{"role":"user", "content":message}], "model":"llama3-8b-8192"}
response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers={"Authorization":f"Bearer {key}", "Content-Type":"application/json"}, json=messageJson)

#TODO: add handling for like bad requests or whatever 


responseStatusCode = response.status_code

if responseStatusCode == 200:
    responseJson = json.loads(response.text)
    responseMessage = responseJson["choices"][0]["message"]["content"]
    print(responseMessage)
else:
    print("request failed with code", responseStatusCode)

"""
# makes program into a proper chatbot
while(True):
    print("any other prompts?")
    newPrompt = input()
    messageJson["messages"].append({"role":"assistant", "content":responseMessage})
    messageJson["messages"].append({"role":"user", "content":newPrompt})
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers={"Authorization":f"Bearer {key}", "Content-Type":"application/json"}, json=messageJson)
    responseJson = json.loads(response.text)
    responseMessage = responseJson["choices"][0]["message"]["content"]
    print(responseMessage)
"""


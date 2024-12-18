import google.generativeai as genai
import sys

assert len(sys.argv) > 1

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("hello")
print(response.text)





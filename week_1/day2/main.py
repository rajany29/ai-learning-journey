import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("my_api_key")

if not my_api_key:
    raise ValueError("Api Key is not found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt = "How can I book a doctor's appointment?"

#system_prompt
system_prompt = {
    "role":"system",
    "content":"You are a helpful hospital receptionist. Answer patient questions politely and provide general hospital-related information."
}

message = {
    "role":role,
    "content":prompt
}

messages = [message,system_prompt]
#tempearture
response = client.chat.completions.create(model=model,messages=messages,temperature=2)
print(response.choices[0].message.content)



import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("my_api_key")

if not my_api_key:
    raise ValueError("Api key is not found")


client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt1 = "hello "
prompt2 = "there is so much noise here"
prompt3 = "here is so slient place available"

prompts = [prompt1,prompt2,prompt3]
for prompt in prompts:
    message = {
    "role":role,
    "content":prompt  
   }
    message = [message]
    response = client.chat.completions.create(model=model,messages=message,max_tokens=5000)
    usage=response.usage
    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")

    

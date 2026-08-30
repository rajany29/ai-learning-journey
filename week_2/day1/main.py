import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "qwen/qwen3.6-27b" 

knowdege = {
    "age":"the age of raj 28",
    "job":"learning ai engineer to want become next 6 months"
}

def retrieve_info(question):
    question = question.lower()
    if 'age' in question:
        return knowdege['age']
    elif 'job' in question:
        return knowdege['job']
    else:
        return None


def ask_llm(question):
    context = retrieve_info(question)

    system_prompt = f"""
    answer in one line only. Answer only based on this context. do not hallucinate. Context: {context}
    """
    system_message = {
        "role" : "system",
        "content":system_prompt
    }

    user_prompt = {
        "role": "user",
        "content": question
    }

    messages = [system_message,user_prompt]

    response=client.chat.completions.create(model=model, messages=messages,reasoning_effort="none")
    answer=response.choices[0].message.content
    return answer

question="what is raj's age?"
print(ask_llm(question))

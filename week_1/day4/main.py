import os
import json
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel , ValidationError

# Load environment variables
load_dotenv()

api_key = os.getenv("my_api_key")

if not api_key:
    raise ValueError("API key not found")

client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"

# -----------------------------
# Pydantic Model
# -----------------------------
class Ticket(BaseModel):
    name: str
    email: str
    phone: str
    address: str


schema = Ticket.model_json_schema()

# -----------------------------
# System Prompt
# -----------------------------
system_prompt = f"""
You are an AI information extraction assistant.
Extract customer information from the provided text.
Return ONLY valid JSON.
Do not add explanations.
Do not add markdown.
Do not use triple backticks.
The JSON must follow this schema exactly:
{schema}
"""

user_prompt = f"""
Extract customer details from the following text.
Return only JSON.
My name is Raj.
My phone number is 9803800000.
My email is rajf@gmail.com.
My address is Mumbai.
my div is a
"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_prompt
    }
]

# -----------------------------
# Generate Response
# -----------------------------
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type": "json_object"},
    temperature=0
)

answer = response.choices[0].message.content

print("\nRaw Response")
print("-" * 40)
print(answer)

# -----------------------------
# Parse JSON
# -----------------------------
try:
    data = json.loads(answer)

    ticket = Ticket(**data)

    print("\nValidated Data")
    print("-" * 40)
    print("Name    :", ticket.name)
    print("Email   :", ticket.email)
    print("Phone   :", ticket.phone)
    print("Address :", ticket.address)

except json.JSONDecodeError:
    print("❌ Invalid JSON received.")

except ValidationError as e:
    print("❌ Validation Error")
    print(e)
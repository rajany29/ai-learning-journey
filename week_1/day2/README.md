# 🏥 AI Hospital Assistant using Groq API

A simple AI-powered Hospital Assistant built with **Python** and the **Groq Python SDK**.

This project demonstrates how **System Prompts** can control the behavior of a Large Language Model (LLM). Instead of acting as a general chatbot, the model behaves like a helpful hospital receptionist by answering healthcare-related questions and providing general hospital guidance.

> ⚠️ This project is for educational purposes only and should not be used for medical diagnosis or treatment.

---

## 🚀 Features

- 🤖 AI-powered Hospital Assistant
- 🏥 Uses System Prompts to define AI behavior
- 💬 Supports interactive user questions
- 🔐 Secure API key management using `.env`
- 🌡️ Adjustable Temperature for response creativity
- 🐍 Built with Python and Groq SDK

---

## 🛠️ Tech Stack

- Python 3.x
- Groq Python SDK
- python-dotenv
- Llama 3.3 70B Versatile

---

## 📂 Project Structure

```text
hospital-ai-assistant/
│
├── hello.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---



### Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install groq python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
my_api_key=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💻 Example Code

```python
message_system = {
    "role": "system",
    "content": "You are a helpful hospital receptionist. Answer patient questions politely and provide general hospital-related information."
}

message = {
    "role": "user",
    "content": "I have a fever and sore throat. What should I do?"
}
```

---

## 🌡️ Temperature

The `temperature` parameter controls the creativity of the AI's responses.

| Temperature | Behavior |
|-------------|----------|
| 0.0 - 0.3 | Very consistent and factual |
| 0.4 - 0.7 | Balanced responses |
| 0.8 - 1.2 | More natural and creative |
| 1.3 - 2.0 | Highly creative and varied |

Example:

```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=0.7
)
```

---

## 🧠 What I Learned

- How to use the Groq Python SDK
- Loading environment variables using `.env`
- Creating chat completions
- Understanding the difference between **System** and **User** prompts
- Using **Temperature** to control AI response style
- Working with the Llama 3.3 70B Versatile model

---

## 📝 Sample Questions

- I have a fever for two days. What should I do?
- Which department should I visit for chest pain?
- What are the symptoms of dengue?
- How do I book a doctor's appointment?
- What precautions should I take after surgery?

---

## 📌 Future Improvements

- Interactive chat interface
- Conversation memory
- Voice input/output
- Appointment booking simulation
- Multiple hospital departments
- Multi-language support

## 👨‍💻 Author

**Rajan Yadav**

Backend Developer | Learning AI & Generative AI

Building AI applications with Python one project at a time.

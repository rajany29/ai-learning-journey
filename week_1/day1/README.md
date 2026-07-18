# Groq AI Chatbot

A simple Python chatbot application built using the **Groq Python SDK** and **Llama 3.3 70B Versatile** model.

## 🚀 Features

- Connects to the Groq API
- Uses the Llama 3.3 70B Versatile model
- Loads API key securely using `.env`
- Simple and beginner-friendly project structure

## 📂 Project Structure

```
.
├── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
|__ pyproject.toml
|__ uv.lock
```

## 🛠️ Prerequisites

- Python 3.10+
- Groq API Key

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/rajany29/AI---Engineer.gits
cd <week_1/day1>
```

### 2. Create a virtual environment

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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install groq python-dotenv
```

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```


## ▶️ Run the Project

```bash
python main.py
```

## 🤖 Model Used

```
llama-3.3-70b-versatile
```

## 📚 Dependencies

- groq
- python-dotenv

## 📄 requirements.txt

Generate it using:

```bash
pip freeze > requirements.txt
```
## 📖 Learning Goals

- Python
- Environment Variables
- Groq SDK
- LLM APIs
- Prompt Engineering

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License.
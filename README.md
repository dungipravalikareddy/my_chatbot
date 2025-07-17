# 🤖 Mystic Bot

Welcome to **Mystic Bot** – an interactive, modular chatbot powered by **OpenAI GPT models**, built with clean architecture principles and a touch of fun. 🌟

---

## ✨ **Project Overview**

This is a **modular, scalable CLI chatbot** designed using:

- **Design Patterns:** Singleton for the OpenAI client
- **Principles:** SOLID (Single Responsibility, Open/Closed, Dependency Inversion)
- **Features:** 
  - Prompt history tracking
  - Config management via `.env`
  - Fun greetings and graceful goodbyes

---

## 🚀 **How to Run**

1. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate    # macOS/Linux
    venv\\Scripts\\activate     # Windows
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure your `.env` file:**

    ```env
    OPENAI_API_KEY=your_real_openai_key_here
    MODEL_NAME=gpt-3.5-turbo
    SYSTEM_PROMPT=You are a helpful assistant.
    ```

4. **Run the chatbot:**

    ```bash
    python main.py
    ```

---

## 🛠️ **Implementation Highlights**

✔ **Singleton Pattern** – ensures a single OpenAI client instance  
✔ **Prompt History Manager** – maintains context across interactions  
✔ **Clean Config Management** – loads secrets safely from `.env`  
✔ **SOLID Principles**:
- **SRP:** each class/module has one responsibility
- **OCP:** extend without modifying existing classes
- **DIP:** high-level modules depend on abstractions
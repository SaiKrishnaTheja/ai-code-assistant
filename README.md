# AI Code Assistant (LangChain + Ollama)

## 🚀 Overview
This project is an AI-powered coding assistant that can:
- 📄 **Document**: Automatically generate docstrings for Python functions/classes.
- ⚡ **Optimize**: Improve performance and readability of Python code.
- 🐞 **Debug**: Identify and fix errors in Python code.

## 📌 Features
- Uses Llama models via LangChain.
- Automatically determines whether to **document, optimize, or debug** code.
- Simple CLI interface for user interaction.

The assistant runs **locally** using the **CodeLlama** model with Ollama, so you must have it installed on your system.

## 🚀 **Installation Guide**

### **1. Install Ollama**
Ollama is required to run CodeLlama locally.  
Download and install Ollama from the official site:

🔗 [Ollama Installation Guide](https://ollama.com)

For macOS and Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 🛠️ Installation for LangChain

### 1️⃣ Install Dependencies
```bash
pip install langchain-community
```

# 🛍️ ItemInsight – AI-Powered Product Info & Price Estimator

**ItemInsight** is a lightweight AI application that delivers concise product summaries and real-time estimated prices in Indian Rupees (INR) using cutting-edge Large Language Models (LLMs). Built with **LangChain**, **Streamlit**, and **OpenAI/Groq**, it's perfect for quick product research and market value estimation.

---

## 📌 Features

- ✅ Accepts any product name input
- 🧠 Utilizes top-tier LLMs (GPT-4.1, Qwen, LLaMA 3) for intelligent responses
- 📦 Returns structured JSON with:
  - **Product Name**
  - **Short Description** (≤150 words)
  - **Estimated Price** in **INR**
- ⚙️ Clean Streamlit UI for interactive exploration
- 🔐 Supports multiple API providers via `.env` config

---

## 🖼️ Sample Output

```json
{
  "name": "MacBook Air M2 (2023)",
  "details": "A lightweight, high-performance laptop powered by Apple’s M2 chip. Offers long battery life, a Retina display, and smooth macOS experience. Suitable for students, creators, and professionals.",
  "price": 115000
}

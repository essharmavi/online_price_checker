# Online Price Checker – Product Info & Price Estimator with LLMs

An AI-powered tool that delivers concise product information and estimated market pricing. Whether you're researching gadgets, services, or memberships, just enter the name — the app returns a clean, structured summary including the name, details, and estimated price in Indian Rupees (INR).

### ✨ Features

🔍 Takes any product name as input
🧠 Uses LLMs (GPT-4.1, Qwen, LLaMA 3) via LangChain
📦 Returns structured JSON with:
Product name
Short description (max ~150 words)
Estimated price in INR
⚙️ Clean Streamlit UI for easy interaction
⚙️ Tech Stack

###Component	Technology
**Language Model**	OpenAI GPT-4.1, Groq Qwen, LLaMA 3
**Interface**	Streamlit
**Backend Logic**	LangChain
**Output Parsing**	Pydantic + LangChain JSON Parser
**Prompt System***	JSON-based PromptTemplate
**Environment**	Python 3.12 + dotenv

from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
import streamlit as st
import json
import time

# Load API keys
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Available models
models_list = ["gpt-4.1", "qwen-qwq-32b", "llama-3.3-70b-versatile"]

st.title("Online Price Estimator")
st.markdown(
    "**Check prices online and get an estimated price plus details of the product**"
)

# Define the Pydantic output schema
class Product(BaseModel):
    name: str = Field(..., description="Get the name of the product")
    details: str = Field(..., description="A small summary of the product")
    price: int = Field(..., description="Estimated price of the product in USD")


# Create the JSON output parser
parser = JsonOutputParser(pydantic_object=Product)
format_instructions = parser.get_format_instructions()

# Load template from JSON file
def load_prompt_template(filepath: str) -> PromptTemplate:
    with open(filepath, "r") as f:
        prompt_json = json.load(f)
    return PromptTemplate(
        template=prompt_json["template"], input_variables=prompt_json["input_variables"]
    )


# Model selection
option = st.selectbox(
    "Please select a model:", models_list, index=None, placeholder="Select a model"
)

# Load LLM
if option:
    if option == "gpt-4.1":
        llm = ChatOpenAI(model=option, temperature=0.0, api_key=openai_api_key)
    else:
        llm = ChatGroq(model=option, temperature=0.0, api_key=groq_api_key)
else:
    st.stop()


# Load prompt
file_path = os.path.join(os.path.dirname(__file__), "template.json")
prompt = load_prompt_template(file_path)
print(prompt)

st.markdown("**Write down your product name here.**")
product_name = st.text_area(
    "Give me the product name", placeholder="Macbook Pro 2017 model", max_chars=50
)

if st.button("Get Info"):
    if not product_name.strip():
        st.warning("Please enter a product name.")
    else:
        with st.spinner("Getting the results..."):
            chain = (
                prompt| llm | parser
            )
            result = chain.invoke(
                {
                    "product_name": product_name,
                    "format_instructions": format_instructions,
                }
            )
            st.subheader("Product Info")
            st.markdown(f"**Name:** {result['name']}")
            st.markdown(f"**Details:** {result['details']}")
            st.markdown(f"**Price (INR):** ₹{result['price']}")

import os
import time
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment
api_key = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=api_key)

# Function to process input text
def process_text(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"You are a helpful assistant that generates names of stars and constellations {input_text}")
    return response.text

# Initialize chat history
chat_history = [
    {"role": "system", "content": "You are a helpful assistant that generates names of stars and constellations."},
]

# Streamlit UI
st.title("Star & Constellation Name Generator")

# User input for the question
user_input = st.text_input("Ask me to generate names of stars or constellations:")

if st.button("Generate"):
    if user_input:
        with st.spinner("Generating..."):
            reply = process_text(user_input)
            st.success("Here are the names:")
            st.write(reply)
    else:
        st.error("Please enter a prompt!")

# Reset button to clear chat history
if st.button("Reset Chat"):
    chat_history = [
        {"role": "system", "content": "You are a helpful assistant that generates names of stars and constellations."}
    ]
    st.success("Chat has been reset.")

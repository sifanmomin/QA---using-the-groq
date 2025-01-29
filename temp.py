import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Groq client
#groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key="you key",
)

# Streamlit UI
st.title("AI Question Answering Bot")

# Input for user query
user_input = st.text_area("Ask a question:", placeholder="Type your question here...")

if st.button("Get Answer") and user_input.strip():
    try:
        # Send user input to the Groq API
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an AI assistant that provides concise and accurate answers to user questions."},
                {"role": "user", "content": user_input},
            ],
            model="llama-3.3-70b-versatile",  # Adjust the model as per your needs
        )
        # Display the response
        answer = response.choices[0].message.content
        st.success("Answer:")
        st.write(answer)
    except Exception as e:
        st.error(f"Failed to retrieve an answer: {str(e)}")

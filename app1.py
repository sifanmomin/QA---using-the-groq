import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()

# Initialize Streamlit session state if vectors haven't been set yet
if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama2:latest")  # Updated model name
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# Streamlit title
st.title("ChatGroq Demo")

# Groq API key initialization (commented out, update when needed)
# groq_api_key = os.environ['GROQ_API_KEY']

# Initialize the ChatGroq model
llm = ChatGroq(groq_api_key="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",
             model_name="mixtral-8x7b-32768")

# Define the prompt template for generating answers based on context
prompt = ChatPromptTemplate.from_template("""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}
""")

# Create document chain for answering queries
document_chain = create_stuff_documents_chain(llm, prompt)

# Setup vector retriever
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Input field for the user to enter a prompt
prompt = st.text_input("Input your prompt here")

# Process the prompt and retrieve the answer if prompt is provided
if prompt:
    start = time.process_time()
    response = retrieval_chain.invoke({"input": prompt})
    st.write("Response time:", time.process_time() - start)
    st.write(response['answer'])

    # Display relevant documents with an expander
    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")

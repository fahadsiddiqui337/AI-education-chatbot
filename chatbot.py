import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st


# Load API Key 
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Load AI Model 
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Streamlit UI Setup
st.title("📚 AI Education Chatbot")
st.write("Ask any question related to your studies!")

# Maintain Chat History  
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful AI tutor.")]

#User Input
query = st.text_input("You: ", "")
if query:
    # Add User message in chat history
    st.session_state.chat_history.append(HumanMessage(content=query))
    
    # Answer from AI
    response = model.invoke(st.session_state.chat_history)
    
    # Add AI response in history
    st.session_state.chat_history.append(AIMessage(content=response.content))
    
    # AI's Answer
    st.write(f"🤖 AI: {response.content}")
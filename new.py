import os
import streamlit as st
import google.generativeai as gen_ai
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Smart Recommendation System",
    page_icon=":brain:",
    layout="wide"
)

# Load the dataset
df = pd.read_csv("companion_plants.csv")

# Set up Google Gemini-Pro AI model
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Function to recommend plants based on user input
def recommend_plants(user_plant):
    matches = df[df['Source Node'] == user_plant]['Destination Node'].tolist()
    return matches

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("Smart Recommendation System")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_input = st.text_input("Enter a plant name:")

if user_input:
    # Display recommendations from CSV
    recommendations = recommend_plants(user_input)
    if recommendations:
        st.write(f"Recommended companion plants for {user_input}:")
        for plant in recommendations:
            st.write(f"- {plant}")
    else:
        st.write("Sorry, no recommendations found for the entered plant.")

    # Construct the query about compatible plants
    full_query = f"{user_input},: what are the pesticides that can be used to grow this plant with other companion plants that are planted with it"

    # Add user's constructed query to chat and display it
    st.chat_message("user").markdown(user_input)

    # Send the constructed query to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(full_query)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

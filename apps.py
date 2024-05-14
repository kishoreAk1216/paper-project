
import pandas as pd

# Load the dataset
df = pd.read_csv("companion_plants.csv")

# Preprocess the data (if needed)

# Function to recommend plants based on user input
def recommend_plants(user_plant):
    matches = df[df['Source Node'] == user_plant]['Destination Node'].tolist()
    return matches
    
import streamlit as st

# Import the recommendation function
from recommend_plants import recommend_plants

# Streamlit UI
st.title("Plant Companion Recommendation")

# Input field for user's message
user_input = st.text_input("Enter a plant name:")

if user_input:
    recommendations = recommend_plants(user_input)
    if recommendations:
        st.write(f"Recommended companion plants for {user_input}:")
        for plant in recommendations:
            st.write(f"- {plant}")
    else:
        st.write("Sorry, no recommendations found for the entered plant.")

# Expose Streamlit app with ngrok
from pyngrok import ngrok
ngrok.set_auth_token("2g9FaFiDvJXXzZBrbGHWUwdZBc2_4DpLLpYhJGx6Lbd8t6EG8")


public_url = ngrok.connect(port='8501')
public_url

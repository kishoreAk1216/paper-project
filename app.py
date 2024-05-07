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

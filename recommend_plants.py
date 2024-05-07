import pandas as pd

# Load the dataset
df = pd.read_csv("companion_plants.csv")

# Preprocess the data (if needed)

# Function to recommend plants based on user input
def recommend_plants(user_plant):
    matches = df[df['Source Node'] == user_plant]['Destination Node'].tolist()
    return matches

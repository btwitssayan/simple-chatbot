import time
import pywhatkit
import pyjokes
import random
import streamlit as st

# Define greetings and responses
greetings = ["hello", "hi", "hey", "howdy", "hola"]

responses = [
    "Hello!",
    "Hi there!",
    "Hey!",
    "Greetings!",
    "Hi! How can I help you?",
]

# Define chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in greetings:
        return random.choice(responses)
    elif "time" in user_input:
        current_time = time.strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "tell me a joke" in user_input:
        joke = pyjokes.get_joke()
        return joke
    elif "search" in user_input: 
        search_query = user_input.replace("search", "").strip()
        if search_query == "":
            return "I'm sorry, you didn't provide a specific query for the search."
        else:
            pywhatkit.search(search_query)
            return "Searching the web for your query..."
    elif "play" in user_input:
        search_query = user_input.replace("play", "").strip()
        pywhatkit.playonyt(search_query)
        return "Playing on Youtube..."
    else:
        return "I'm sorry, I didn't understand that."

# Streamlit UI
st.title("Chatbot with Streamlit")

# Add instructions
st.write("**Instructions:**")
st.write("1. To search a query, start your input with the keyword 'search'.")
st.write("2. To hear a joke, type 'tell me a joke'.")
st.write("3. To get the current time, include the word 'time' in your input.")
st.write("4. To play a video on YouTube, start your input with 'play'.")
st.write("5. For greetings, you can say 'hello', 'hi', 'hey', 'howdy', or 'hola'.")

# Text input for user input
user_input = st.text_input("You: ", "")

# Check if there is any user input
if user_input:
    response = chatbot_response(user_input)
    st.write("Chatbot:", response)

# Exit condition
if st.button("Exit"):
    st.stop()


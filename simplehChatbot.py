import google.generativeai as genai
import streamlit as st

# Configure the Google API key
Google_api_key = "AIzaSyCuXorhJ17-qmiABnrJz5_PzbJ0F_8HBE0"
genai.configure(api_key=Google_api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the function to get a response from the model
def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit app setup
st.title("⚡Simple Chatbot⚡")
st.write("Powered by Google Generative AI")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Display the chat history above the input form
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for sender, message in st.session_state.history:
    if sender == "User":
        st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-response">{message}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Add some custom styling for chat bubbles
st.markdown(
    """
    <style>
    .user-message {
        background-color: #DCF8C6;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word;
    }
    .bot-response {
        background-color: #ECECEC;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word;
    }
    .chat-container {
        max-width: 600px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Form to take user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000, placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = getResponseFromModel(user_input)
            st.session_state.history.append(("User", user_input))
            st.session_state.history.append(("Bot", response))
        else:
            st.warning("Please enter a prompt!")

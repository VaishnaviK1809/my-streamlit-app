import streamlit as st
import openai
import sqlite3

# Set your DeepAI API key
openai.api_key = '9f72062e-bd7f-4d48-a808-874a0b598af5'

# Initialize the database
def init_db():
    conn = sqlite3.connect('data/your_database.db')
    c = conn.cursor()
    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Save a user interaction
def save_interaction(user_input, response):
    conn = sqlite3.connect('data/your_database.db')
    c = conn.cursor()
    c.execute('INSERT INTO interactions (user_input, response) VALUES (?, ?)',
              (user_input, response))
    conn.commit()
    conn.close()

# Initialize the database when app starts
init_db()

# Streamlit app layout
st.title("AI Chat with DeepAI and SQLite")

# User input
user_input = st.text_area("Enter your message:")

if st.button("Send"):
    if user_input.strip() != "":
        try:
            # Call DeepAI API
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
            # Display response
            st.markdown(f"**AI Response:** {answer}")
            # Save interaction
            save_interaction(user_input, answer)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message.")

# Show past interactions
if st.checkbox("Show past interactions"):
    conn = sqlite3.connect('data/your_database.db')
    c = conn.cursor()
    c.execute("SELECT user_input, response FROM interactions ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    for i, (inp, resp) in enumerate(rows, 1):
        st.write(f"**User:** {inp}")
        st.write(f"**AI:** {resp}")
        st.write("---")import streamlit as st
import openai
import sqlite3

# Set your DeepAI API key
openai.api_key = '9f72062e-bd7f-4d48-a808-874a0b598af5'

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('data/your_database.db')
    c = conn.cursor()
    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to save interaction
def save_interaction(user_input, response):
    conn = sqlite3.connect('data/your_database.db')
    c = conn.cursor()
    c.execute('INSERT INTO interactions (user_input, response) VALUES (?, ?)',
              (user_input, response))
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Streamlit app layout
st.title("AI Chat with DeepAI and SQLite")

# User input
user_input = st.text_area("Enter your message:")

if st.button("Send"):
    if user_input.strip() != "":
        # Call DeepAI API
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
            
            # Display response
            st.markdown(f"**AI Response:** {answer}")
            
            # Save interaction
            save_interaction(user_input, answer)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message.")

# Optional: Display past interactions
if st.checkbox("Show past interactions"):
    conn = sqlite3.connect('data/your_database.db')
    c = conn.cursor()
    c.execute("SELECT user_input, response FROM interactions ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    
    for i, (inp, resp) in enumerate(rows, 1):
        st.write(f"**User:** {inp}")
        st.write(f"**AI:** {resp}")
        st.write("---")import streamlit as st

st.title("My Streamlit App")
st.write("Hello, world!")

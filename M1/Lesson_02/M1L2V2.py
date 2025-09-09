from dotenv import load_dotenv
import openai
import streamlit as st

load_dotenv()

st.title("Game Ecomony Advisor")
st.write("I am a game ecomony advisor. I am here to help you until I will replace you.")

client = openai.OpenAI()
try:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "user", "content": "Explain Game Ecomony in mobile games in 60 words."}  # Prompt
        ],
        temperature=0.7,  # A bit of creativity
        max_output_tokens=100  # Limit response length
    )
    st.write(response.output[0].content[0].text)
except Exception as e:
    st.error(f"API call failed: {e}")


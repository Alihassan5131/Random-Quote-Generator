import streamlit as st
import random

st.title("Random Quote Generator")

quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Happiness depends upon ourselves. – Aristotle"
]

if st.button("Generate Quote"):
    st.write(random.choice(quotes))

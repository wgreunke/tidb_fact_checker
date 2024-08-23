# import streamlit as st
# st.write("Hello world")
# statement=st.text_input("Please enter a fact to check:")

# st.write(statement)

import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
import time

# Inject CSS to set the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;  /* Light Blue Color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Medical Fact Checker")

user_input = st.text_input("Enter a medical fact:")

if st.button("Check Fact"):
    # Show the first message
    with st.spinner("Looking into TiDB..."):
        time.sleep(2)  # Simulate some delay, replace with your actual TiDB query or processing
        # Perform your TiDB related processing here

    # Show the second message
    with st.spinner("LLM is thinking..."):
        time.sleep(2)  # Simulate some delay, replace with your actual LLM processing

#Chunk fact

#Send fact to tidb

#Show search results

#Send to llm

#Show whether true or false.
#Show source of document / add link to source


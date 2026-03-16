import streamlit as st
from dotenv import load_dotenv
import os
from main import process_image


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Please check the OPENAI_API_KEY.")

def scanner():
    st.title("Scanner")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("Processing the image...")

        result = process_image(uploaded_file)
        st.subheader("Product Details")
        st.write(result)

    else:
        st.write("Please upload an image to scan.")

    
if __name__ == "__main__":
    scanner()
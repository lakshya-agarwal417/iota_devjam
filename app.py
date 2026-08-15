import streamlit as st
from logic import generate_study_notes

st.set_page_config(page_title="Study Simplifier", page_icon="📚")
st.title("📚 Quick Study Simplifier")

user_notes = st.text_area("Paste your study material here:", height=150)

if st.button("Generate Summary"):
    if user_notes.strip():
        with st.spinner("Processing with AI..........."):
            result = generate_study_notes(user_notes)
            st.success("Here is your summary:")
            st.write(result)
    else:
        st.warning("Please paste some text first!")

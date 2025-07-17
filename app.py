import streamlit as st
from prompt_generator import generate_best_prompt

st.set_page_config(page_title="🧠 Smart Prompt Generator", layout="centered")

st.title("🧠 Smart Prompt Generator")
st.markdown("Enter a **word**, idea, or task. I’ll craft the best prompt for you!")

user_input = st.text_input("Enter your idea or keyword")

# 🔽 New: Tone and Category dropdowns
tone = st.selectbox("Choose a tone", ["Neutral", "Professional", "Friendly", "Funny", "Persuasive"])
category = st.selectbox("Select a category", ["General", "Blogging", "Coding", "Marketing", "Education", "Startup Ideas"])

if user_input:
    with st.spinner("Crafting the perfect prompt..."):
        result = generate_best_prompt(user_input, tone, category)
    st.markdown("### 🪄 Optimized Prompt:")
    st.code(result, language='markdown')

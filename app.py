import os
import streamlit as st
from data.questions import questions

# ✅ Set page config first
st.set_page_config(page_title="Q&A Explorer", layout="wide")

# ✅ Load and inject CSS
style_path = os.path.join(os.path.dirname(__file__), "styles", "style.css")
with open(style_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ App Title
st.markdown("<h1 style='color:#FB8C00;'>💬 Q & A Explorer – OpenAI Agents SDK</h1>", unsafe_allow_html=True)

st.markdown("---")

# ✅ Loop through Q&A
for idx, qa in enumerate(questions, 1):
    st.markdown(f"""
        <div class='qa-line'>
            <div class='question'>❓ <strong>Question {idx}:</strong> {qa['question']}</div>
            <div class='answer'>✅ <strong>Answer:</strong> {qa['answer']}</div>
            <div class='example'>💡 <strong>Example:</strong> {qa.get("example", "")}</div>
        </div>
        <hr>
    """, unsafe_allow_html=True)

# ✅ Brief Info Section
st.markdown("---")
st.markdown("<h3 style='color:#FB8C00;'>📘 About OpenAI & Agents SDK</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size:20px; line-height:1.6;'>
<b>1. 🧠 OpenAI</b><br>
OpenAI is an AI research and deployment company known for developing advanced models like <b>ChatGPT</b> and <b>GPT-4</b>.<br>
It creates tools that help people and businesses use artificial intelligence responsibly and powerfully.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size:20px; line-height:1.6;'>
<b>2. 🤖 Agents SDK (OpenAI)</b><br>
The Agents SDK is a tool by OpenAI that helps developers build <b>AI-powered agents</b> that can use functions, tools, and context to reason, take actions, and return results — like a smart assistant that can run code, call APIs, or answer questions.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)


# ✅ Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue;'>🎓 Mentor: <i>Sir. Aneeq Khatri</i></h4>", unsafe_allow_html=True)
st.markdown("<h4 style='color:red;'>✍️ Author: <i>Azmat Ali Akbar</i></h4>", unsafe_allow_html=True)




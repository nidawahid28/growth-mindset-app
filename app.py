# streamlit
import streamlit as st
from datetime import datetime

# Page configuration with custom theme
st.set_page_config(
    page_title="Growth Mindset Journey",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton button {
        width: 100%;
        border-radius: 20px;
    }
    .success-box {
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #28a745;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Main title with animation
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🌱 Your Growth Mindset Journey 🌱</h1>", unsafe_allow_html=True)

# Motivational quotes carousel
quotes = [
    {"quote": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Everything is possible. The impossible just takes longer.", "author": "Dan Brown"}
]

# Display random quote in a styled container
st.markdown("""
    <div style='padding: 20px; background-color: #f0f2f6; border-radius: 10px; text-align: center;'>
        <h3>✨ Daily Inspiration ✨</h3>
    </div>
""", unsafe_allow_html=True)
quote_idx = datetime.now().day % len(quotes)
st.markdown(f"<p style='text-align: center; font-style: italic;'>'{quotes[quote_idx]['quote']}'</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>- {quotes[quote_idx]['author']}</p>", unsafe_allow_html=True)

# Create three columns for main sections
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center;'>🎯 Today's Challenge</h3>", unsafe_allow_html=True)
    user_challenge = st.text_area("What challenge will you tackle today?")
    if user_challenge:
        st.markdown(f"""
            <div class='success-box'>
                <p>Your challenge: {user_challenge}</p>
                <p>💪 You've got this!</p>
            </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='text-align: center;'>🤔 Daily Reflection</h3>", unsafe_allow_html=True)
    reflection = st.text_area("What did you learn today?")
    if reflection:
        st.markdown(f"""
            <div class='success-box'>
                <p>Your reflection: {reflection}</p>
                <p>✨ Great insights!</p>
            </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("<h3 style='text-align: center;'>🏆 Achievements</h3>", unsafe_allow_html=True)
    achievement = st.text_area("What have you achieved today?")
    if achievement:
        st.markdown(f"""
            <div class='success-box'>
                <p>Your achievement: {achievement}</p>
                <p>🎉 Congratulations!</p>
            </div>
        """, unsafe_allow_html=True)

# Progress tracker
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>📈 Weekly Progress</h3>", unsafe_allow_html=True)
progress = st.progress(0)
mood = st.select_slider(
    "How are you feeling about your progress?",
    options=["😔", "😐", "🙂", "😊", "🤩"],
    value="🙂"
)
progress.progress({"😔": 20, "😐": 40, "🙂": 60, "😊": 80, "🤩": 100}[mood])

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center;'>
        <p>🌱 Nurture your growth mindset every day! 🌱</p>
        <p style='font-size: 0.8em;'>© 2024 Growth Mindset Journey. All Rights Reserved.</p>
    </div>
""", unsafe_allow_html=True) 

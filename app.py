# import streamlit as st
# import time
# import random

# # Page Configurations
# st.set_page_config(page_title="Growth Mindset Project", page_icon="🌱", layout="wide")

# # Custom Styling
# st.markdown("""
#     <style>
#         .main-header {
#             text-align: center;
#             font-size: 36px;
#             color: #4CAF50;
#             font-weight: bold;
#         }
#         .highlight {
#             font-size: 20px;
#             color: #555;
#         }
#         textarea, input {
#             border-radius: 10px !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown("<h1 class='main-header'>🚀 Growth Mindset Challenge</h1>", unsafe_allow_html=True)
# st.markdown("<p class='highlight'>Embrace challenges, learn from mistakes, and unlock your full potential! ✨</p>", unsafe_allow_html=True)

# # Layout Sections
# col1, col2 = st.columns(2)

# # Growth Mindset Quote
# with col1:
#     st.header("🌻 Today's Growth Mindset Quote")
#     st.info("\"The only limit to our realization of tomorrow will be our doubts of today.\" - Franklin D. Roosevelt")

# # User's Challenge Input
# with col2:
#     st.header("🔧 What's Your Challenge Today?")
#     user_input = st.text_input("📝 Enter your challenge:")
#     submit_button = st.button("Submit Challenge", disabled=not user_input)
#     if submit_button:
#         st.success(f"🚀 Your challenge: {user_input}. Keep pushing forward! 💪")

# # Reflection Section
# st.header("🌟 Reflect on Your Growth Journey")
# reflection = st.text_area("📖 Write your reflection:")

# # Achievement Section
# st.header("🏆 Today's Achievement")
# achievement = st.text_input("🎉 Enter your achievement:")

# # Dynamic Motivation Messages
# motivational_quotes = [
#     "✨ Remember: Every expert was once a beginner. Keep going! 🚀",
#     "💡 Growth starts outside of your comfort zone! Keep pushing forward! 💪",
#     "🌱 Success is the sum of small efforts repeated daily! Keep going! 🎯",
#     "🚀 Your mindset shapes your reality. Stay positive, stay growing! 🌟",
#     "🔥 Challenges are opportunities in disguise. Face them with courage! 💪"
# ]

# if st.button("💡 Need Motivation?"):
#     with st.spinner("Fetching motivation..."):
#         time.sleep(2)
#     st.success(random.choice(motivational_quotes))

# # Progress Tracking
# st.header("📊 Your Progress")
# total_sections = 3
# completed_sections = sum(bool(text) for text in [user_input, reflection, achievement])
# progress = completed_sections / total_sections
# st.progress(progress)

# # Footer
# st.write("- - -")
# st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
# st.write("Ⓒ 2025 Growth Mindset Challenge. All Rights Reserved.")


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
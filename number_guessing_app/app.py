import streamlit as st
import random
import time
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# ---------------- SOUND EFFECTS ----------------
def play_sound(success=True):
    if success:
        sound = "UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQAAAAA="
    else:
        sound = "UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQAAAAA="
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/wav;base64,{sound}" type="audio/wav">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #00e5ff;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #b0bec5;
    }
    .success-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #1b5e20;
        color: white;
        text-align: center;
        font-size: 18px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🎯 Number Guessing Game</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">With Difficulty, Timer, Scoreboard & Sound</div>', unsafe_allow_html=True)
st.divider()

# ---------------- SESSION STATE INIT ----------------
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.scoreboard = []

# ---------------- DIFFICULTY SELECTION (1️⃣) ----------------
difficulty = st.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

if difficulty == "Easy":
    max_number = 50
    max_attempts = 10
elif difficulty == "Medium":
    max_number = 100
    max_attempts = 7
else:
    max_number = 200
    max_attempts = 5

# ---------------- START GAME ----------------
if st.button("▶ Start Game", use_container_width=True) and not st.session_state.started:
    st.session_state.number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.start_time = time.time()
    st.session_state.game_over = False
    st.session_state.started = True

# ---------------- GAME LOGIC ----------------
if st.session_state.started and not st.session_state.game_over:

    st.info(f"🎯 Guess a number between 1 and {max_number}")
    st.info(f"🧮 Remaining Attempts: {max_attempts - st.session_state.attempts}")

    guess = st.number_input(
        "Enter your guess",
        min_value=1,
        max_value=max_number,
        step=1
    )

    if st.button("🎲 Submit Guess", use_container_width=True):
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning("📉 Too Low!")
            play_sound(False)

        elif guess > st.session_state.number:
            st.warning("📈 Too High!")
            play_sound(False)

        else:
            elapsed_time = round(time.time() - st.session_state.start_time, 2)
            st.session_state.game_over = True

            # 3️⃣ SCOREBOARD
            st.session_state.scoreboard.append({
                "Difficulty": difficulty,
                "Attempts": st.session_state.attempts,
                "Time (s)": elapsed_time
            })

            play_sound(True)

            st.markdown(
                f"<div class='success-box'>🎉 Correct!<br>"
                f"Attempts: {st.session_state.attempts}<br>"
                f"Time: {elapsed_time} seconds</div>",
                unsafe_allow_html=True
            )

        if st.session_state.attempts >= max_attempts and not st.session_state.game_over:
            st.session_state.game_over = True
            st.error(f"❌ Game Over! The number was {st.session_state.number}")

# ---------------- SCOREBOARD DISPLAY (3️⃣) ----------------
if st.session_state.scoreboard:
    st.divider()
    st.subheader("🏆 Scoreboard")
    st.table(st.session_state.scoreboard)

# ---------------- RESTART ----------------
st.divider()
if st.button("🔄 Restart Game", use_container_width=True):
    st.session_state.clear()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Python • Streamlit • Game Project</p>",
    unsafe_allow_html=True
)

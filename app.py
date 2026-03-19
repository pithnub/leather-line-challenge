import streamlit as st

st.set_page_config(page_title="Leather Line Challenge", layout="wide")

st.title("🧪 Leather Line Challenge")
st.write("Make the right decisions to produce high-quality leather.")

# Hidden state
if "score" not in st.session_state:
    st.session_state.score = 0

# Helper function
def question(prompt, options, correct, explanation):
    st.subheader(prompt)
    choice = st.radio("Select your action:", options, key=prompt)
    if st.button("Submit", key=prompt+"btn"):
        if choice == correct:
            st.success("Correct")
            st.session_state.score += 10
        else:
            st.error("Not ideal")
            st.session_state.score -= 5
        st.info(explanation)

# Stage 1
question(
    "Stage 1: Leather feels firm after drying",
    ["Send to staking", "Condition leather", "Dry further", "Send to finishing"],
    "Condition leather",
    "Leather must be correctly conditioned before staking to allow fibre movement."
)

# Stage 2
question(
    "Stage 2: Ready for softening",
    ["Increase temperature only", "Stake correctly", "Dry drum immediately", "Finish"],
    "Stake correctly",
    "Staking develops softness through fibre movement."
)

# Stage 3
question(
    "Stage 3: Soft but uneven",
    ["Ignore", "Re-condition and re-stake", "Finish", "Dry further"],
    "Re-condition and re-stake",
    "Uneven softness requires reprocessing."
)

# Stage 4
question(
    "Stage 4: Upholstery leather target",
    ["Skip drumming", "Light drum", "Controlled dry drum", "Heavy dry"],
    "Controlled dry drum",
    "Dry drumming develops softness and grain character."
)

# Stage 5
question(
    "Stage 5: Pebble but slightly loose",
    ["Continue drumming", "Reduce and stabilise", "Add moisture", "Finish"],
    "Reduce and stabilise",
    "Over-drumming risks loose grain."
)

# Stage 6
question(
    "Stage 6: Final prep",
    ["Send to finishing", "Toggle dry", "Re-stake", "Drum again"],
    "Send to finishing",
    "Leather is ready when softness, grain, and moisture are correct."
)

st.write("---")
st.subheader("Final Score")
st.write(st.session_state.score)

if st.session_state.score >= 50:
    st.success("Excellent processing decisions")
elif st.session_state.score >= 20:
    st.warning("Good, but some improvements needed")
else:
    st.error("Process needs improvement")

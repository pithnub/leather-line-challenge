import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Leather Line Challenge", layout="wide")

st.title("🧪 Leather Line Challenge")
st.markdown("### 🎯 Your Goal: Produce leather ready for finishing")

st.info("""
You are responsible for preparing leather for finishing.

Your decisions will affect:
- softness
- grain quality
- fibre structure
- consistency

Make the right calls at each stage.
""")

# --- STATE INITIALISATION ---
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.moisture = 50
    st.session_state.softness = 50
    st.session_state.grain = 50
    st.session_state.structure = 50

# --- SIDEBAR: PRODUCT TARGET ---
st.sidebar.header("🎯 Production Target")

product = st.sidebar.selectbox(
    "Select Leather Type:",
    ["Upholstery", "Shoe Upper", "Garment"]
)

# --- HELPER FUNCTION ---
def update_state(choice, correct, effects):
    if choice == correct:
        st.success("✅ Good decision")
        st.session_state.score += 10
    else:
        st.error("❌ Not ideal")
        st.session_state.score -= 5

    # Apply effects
    for key, value in effects.items():
        st.session_state[key] += value


# =========================
# STAGE 1 — CONDITIONING
# =========================
st.subheader("Stage 1 — Conditioning")

q1 = st.radio(
    "Leather feels slightly firm after drying:",
    ["Send to staking", "Condition leather", "Dry further", "Send to finishing"]
)

if st.button("Submit Stage 1"):
    update_state(
        q1,
        "Condition leather",
        {"moisture": +15, "structure": +5}
    )


# =========================
# STAGE 2 — STAKING
# =========================
st.subheader("Stage 2 — Staking")

q2 = st.radio(
    "Leather is conditioned. What next?",
    ["Increase temperature only", "Stake correctly", "Dry drum immediately", "Send to finishing"]
)

if st.button("Submit Stage 2"):
    update_state(
        q2,
        "Stake correctly",
        {"softness": +15, "structure": +10}
    )


# =========================
# STAGE 3 — SOFTNESS CHECK
# =========================
st.subheader("Stage 3 — Softness Assessment")

q3 = st.radio(
    "Leather is soft but uneven:",
    ["Ignore", "Re-condition and re-stake", "Send to finishing", "Dry further"]
)

if st.button("Submit Stage 3"):
    update_state(
        q3,
        "Re-condition and re-stake",
        {"softness": +10, "structure": +10}
    )


# =========================
# STAGE 4 — DRY DRUMMING
# =========================
st.subheader("Stage 4 — Dry Drumming")

q4 = st.radio(
    "Target: " + product,
    ["Skip drumming", "Light drumming", "Controlled dry drumming", "Heavy drying"]
)

correct_q4 = "Controlled dry drumming" if product != "Shoe Upper" else "Light drumming"

if st.button("Submit Stage 4"):
    update_state(
        q4,
        correct_q4,
        {"softness": +10, "grain": +15}
    )


# =========================
# STAGE 5 — GRAIN CONTROL
# =========================
st.subheader("Stage 5 — Grain Assessment")

q5 = st.radio(
    "Pebble visible but slightly loose:",
    ["Continue drumming", "Reduce and stabilise", "Add moisture", "Send to finishing"]
)

if st.button("Submit Stage 5"):
    update_state(
        q5,
        "Reduce and stabilise",
        {"grain": +10, "structure": +10}
    )


# =========================
# STAGE 6 — FINAL STEP
# =========================
st.subheader("Stage 6 — Final Preparation")

q6 = st.radio(
    "Leather is balanced and ready:",
    ["Send to finishing", "Toggle dry", "Re-stake", "Drum again"]
)

if st.button("Submit Stage 6"):
    update_state(
        q6,
        "Send to finishing",
        {"structure": +5}
    )


# =========================
# RESULTS SECTION
# =========================
st.write("---")
st.header("🔬 Analytical Lab Report")

col1, col2 = st.columns(2)

# --- Lab Analysis ---
with col1:
    st.markdown("### Fibre Structure")
    if st.session_state.structure > 70:
        st.success("Well supported, open fibre structure")
    elif st.session_state.structure > 40:
        st.warning("Moderate fibre support")
    else:
        st.error("Poor structure — risk of loose grain")

    st.markdown("### Softness")
    if st.session_state.softness > 70:
        st.success("Soft, flexible handle")
    elif st.session_state.softness > 40:
        st.warning("Moderate softness")
    else:
        st.error("Firm / boardy handle")

    st.markdown("### Grain Quality")
    if st.session_state.grain > 70:
        st.success("Tight, well-developed grain")
    elif st.session_state.grain > 40:
        st.warning("Acceptable grain")
    else:
        st.error("Loose or uneven grain")


# --- Feedback ---
with col2:
    st.markdown("### Factory Feedback")

    score = st.session_state.score

    if score >= 50:
        st.success(f"Score: {score}/60 — Process Engineer Level")
    elif score >= 20:
        st.warning(f"Score: {score}/60 — Operator Level")
    else:
        st.error(f"Score: {score}/60 — Needs Further Training")

    st.markdown("### Observations")

    if st.session_state.moisture < 40:
        st.write("⚠️ Leather too dry during processing")
    if st.session_state.grain < 40:
        st.write("⚠️ Grain looseness detected")
    if st.session_state.softness < 40:
        st.write("⚠️ Insufficient softening")

    st.markdown("### Handle Assessment")

    if st.session_state.softness > 70 and st.session_state.structure > 60:
        st.write("Excellent handle with good support")
    elif st.session_state.softness > 50:
        st.write("Acceptable handle")
    else:
        st.write("Harsh or inconsistent handle")


# =========================
# RESET BUTTON
# =========================
st.write("---")

if st.button("🔄 Restart Simulation"):
    st.session_state.score = 0
    st.session_state.moisture = 50
    st.session_state.softness = 50
    st.session_state.grain = 50
    st.session_state.structure = 50

st.write("💡 Every decision affects the final leather.")

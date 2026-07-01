import streamlit as st

from detector import analyze_prompt
from risk_engine import calculate_risk

st.set_page_config(
    page_title="SentinelAI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SentinelAI")
st.subheader("AI Prompt Security Scanner")

prompt = st.text_area(
    "Paste your prompt below:",
    height=180
)

if st.button("Analyze Prompt"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:

        detections = analyze_prompt(prompt)

        score, level = calculate_risk(detections)

        st.markdown("---")

        st.metric("Risk Score", score)

        st.metric("Severity", level)

        if detections:

            st.error("Threats Detected")

            for item in detections:
                st.write(f"• {item[0]} → `{item[1]}`")

        else:

            st.success("No threats detected.")

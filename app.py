
import streamlit as st
import joblib

model = joblib.load("cybershield_model.pkl")

st.set_page_config(
    page_title="CyberShield",
    page_icon="🛡️"
)

st.title("🛡️ CyberShield")
st.subheader("Machine Learning SMS Detector")

st.write(
    "Enter a message to check whether "
    "it resembles spam or a legitimate SMS."
)

message = st.text_area("Enter your message:")

if st.button("Analyze Message"):
    if message.strip():
        result = model.predict([message])[0]

        if result == "spam":
            st.error("⚠️ Spam-like message detected!")
        else:
            st.success("✅ Classified as legitimate-like.")

        st.caption(
            "This prediction is not a guarantee of safety."
        )
    else:
        st.warning("Please enter a message.")

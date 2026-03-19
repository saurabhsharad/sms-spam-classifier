import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):
    if input_sms.strip() != "":
        transformed = vectorizer.transform([input_sms])
        result = model.predict(transformed)[0]

        if result == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")
    else:
        st.warning("Please enter a message")
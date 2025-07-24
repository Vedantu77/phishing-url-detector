import streamlit as st
import pickle
import numpy as np
import re

# Hide Streamlit UI for clean appearance
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
    .stDeployButton {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load your trained phishing detection model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Feature extraction from URL
def extract_features(url):
    features = []
    features.append(len(url))
    features.append(int(bool(re.search(r'https://', url))))
    features.append(url.count('.'))
    features.append(int(bool(re.search(r'\d', url))))
    features.append(int(bool(re.search(r'-', url))))
    features.append(int(bool(re.search(r'@', url))))
    return np.array(features).reshape(1, -1)

# UI
st.markdown(
    """
    <h1 style='text-align: center; font-size: 3em;'>🔒 Phishing URL Detector</h1>
    <p style='text-align: center; color: #6c757d; font-size: 1.2em;'>
    Enter a URL below to check if it is <strong>phishing</strong> or <strong>legitimate</strong> using AI detection.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    url_input = st.text_input(" ", placeholder="Paste or type the URL here...")
    check = st.button("🚀 Check URL")

    if check and url_input != "":
        features = extract_features(url_input)
        prediction = model.predict(features)[0]
        
        if prediction == 1:
            st.success("✅ This URL is **legitimate**.")
        else:
            st.error("⚠️ Warning: This URL is **phishing**.")

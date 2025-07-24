import streamlit as st
import pandas as pd
import joblib
from urllib.parse import urlparse
import socket

# Load the model
model = joblib.load('phishing_model.joblib')

# Feature extraction function
def has_ip_address(url):
    try:
        hostname = urlparse(url).hostname
        socket.inet_aton(hostname)
        return 1
    except:
        return 0

def extract_features(url):
    parsed = urlparse(url)
    features = {
        'url_length': len(url),
        'https': int(parsed.scheme == 'https'),
        'has_at': int('@' in url),
        'num_dots': parsed.netloc.count('.'),
        'num_hyphens': parsed.netloc.count('-'),
        'num_subdirs': url.count('/') - 2,
        'has_ip': has_ip_address(url)
    }
    return pd.DataFrame([features])

# Streamlit UI
st.title("🔒 Phishing URL Detector")
url_input = st.text_input("Enter a URL to check:", "")

if st.button("Check URL"):
    if url_input:
        features = extract_features(url_input)
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.error("🚨 This URL is likely a PHISHING URL.")
        else:
            st.success("✅ This URL appears to be LEGITIMATE.")
    else:
        st.warning("⚠️ Please enter a URL to check.")

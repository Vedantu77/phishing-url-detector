import streamlit as st
import pandas as pd
import joblib
import re
from urllib.parse import urlparse

# Load the trained model
model = joblib.load('phishing_model.pkl')

# Feature extraction function
def extract_features_from_url(url):
    features = {}
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['has_at_symbol'] = 1 if '@' in url else 0
    domain = urlparse(url).netloc
    features['has_hyphen'] = 1 if '-' in domain else 0
    features['uses_https'] = 1 if urlparse(url).scheme == 'https' else 0
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'free', 'verify', 'bank', 'webscr']
    features['suspicious_words_count'] = sum(1 for word in suspicious_keywords if word in url.lower())
    features['num_subdomains'] = len(domain.split('.')) - 2 if len(domain.split('.')) > 2 else 0
    ip_pattern = r'((\d{1,3}\.){3}\d{1,3})'
    features['is_ip'] = 1 if re.search(ip_pattern, domain) else 0
    return pd.DataFrame([features])

# Streamlit App UI
st.title("🔒 Phishing URL Detector")
st.write("Check if a URL is **phishing or legitimate** using your trained ML model.")

input_url = st.text_input("Enter the URL to check:")

if st.button("Check URL"):
    if input_url.strip() == "":
        st.warning("Please enter a URL.")
    else:
        features_df = extract_features_from_url(input_url)
        prediction = model.predict(features_df)[0]
        if prediction == 1:
            st.error("🚨 This URL is **Phishing**.")
        else:
            st.success("✅ This URL is **Legitimate**.")

import sqlite3
import pandas as pd
import re
from urllib.parse import urlparse

# Connect to the SQLite database
conn = sqlite3.connect('database/phishing_data.db')
cursor = conn.cursor()

# Read URLs from the phishing_urls table
df = pd.read_sql_query("SELECT * FROM phishing_urls", conn)

print("✅ Loaded URLs from database.")

# Feature extraction function
def extract_features(url):
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
    return features

# Apply feature extraction
features_df = df['url'].apply(lambda x: pd.Series(extract_features(x)))

# Add the label column
features_df['label'] = df['label']

# Store extracted features in a new table
features_df.to_sql('phishing_features', conn, if_exists='replace', index=False)

print("✅ Feature extraction completed and stored in database table 'phishing_features'.")

conn.close()

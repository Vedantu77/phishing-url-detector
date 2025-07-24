import pandas as pd
from urllib.parse import urlparse

# Load dataset
df = pd.read_csv('dataset/phishing_dataset.csv')

# Feature extraction function
def extract_features(url):
    parsed = urlparse(url)
    features = {
        'url_length': len(url),
        'has_at': '@' in url,
        'has_ip': parsed.hostname.replace('.', '').isdigit() if parsed.hostname else False,
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_subdirs': url.count('/'),
        'https': parsed.scheme == 'https',
    }
    return features

# Apply feature extraction
features = df['url'].apply(extract_features).apply(pd.Series)
labels = df['label']

# Save
features.to_csv('dataset/features.csv', index=False)
labels.to_csv('dataset/labels.csv', index=False)

print("[✅] Feature extraction complete. Saved 'features.csv' and 'labels.csv'.")

import pandas as pd

# Load dataset
df = pd.read_csv('dataset/phishing_dataset.csv')

# Feature engineering
df['url_length'] = df['url'].apply(len)
df['has_https'] = df['url'].apply(lambda x: int('https://' in x))
df['num_dots'] = df['url'].apply(lambda x: x.count('.'))
df['has_numbers'] = df['url'].apply(lambda x: int(any(char.isdigit() for char in x)))
df['has_hyphen'] = df['url'].apply(lambda x: int('-' in x))
df['has_at'] = df['url'].apply(lambda x: int('@' in x))

# Keep features + target
features = df[['url_length', 'has_https', 'num_dots', 'has_numbers', 'has_hyphen', 'has_at']]
labels = df['label']

# Save features and labels for model training
features.to_csv('dataset/features.csv', index=False)
labels.to_csv('dataset/labels.csv', index=False)

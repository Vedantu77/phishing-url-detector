import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Prepare training data with the exact same features as in your app
data = pd.read_csv('phishing_dataset.csv')

# Ensure these columns exactly match extract_features output
features = data[[
    'url_length',
    'https',
    'has_at',
    'num_dots',
    'num_hyphens',
    'num_subdirs',
    'has_ip'
]]

labels = data['label']  # Ensure your CSV has a 'label' column

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(features, labels)

joblib.dump(model, 'phishing_model.joblib')
print("✅ Model trained and saved successfully using joblib.")

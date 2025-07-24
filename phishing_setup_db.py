import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load feature and label datasets
features = pd.read_csv('dataset/features.csv')
labels = pd.read_csv('dataset/labels.csv')

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(features, labels.values.ravel())

# Save trained model
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")

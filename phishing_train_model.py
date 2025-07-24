import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Connect to SQLite database
conn = sqlite3.connect('database/phishing_data.db')

# Load extracted features
df = pd.read_sql_query("SELECT * FROM phishing_features", conn)

# Prepare features (X) and labels (y)
X = df.drop(columns=['label'])
y = df['label']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained with accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(clf, 'phishing_model.pkl')
print("✅ Trained model saved as 'phishing_model.pkl'.")

conn.close()

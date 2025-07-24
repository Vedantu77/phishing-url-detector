import sqlite3
import os

# Ensure the 'database' folder exists
if not os.path.exists('database'):
    os.makedirs('database')

# Connect to (or create) the SQLite database
conn = sqlite3.connect('database/phishing_data.db')
cursor = conn.cursor()

# Create the phishing_urls table
cursor.execute('''
CREATE TABLE IF NOT EXISTS phishing_urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    label INTEGER NOT NULL
)
''')

# Sample phishing and legitimate URLs to insert (for testing)
sample_data = [
    ('http://www.google.com', 0),
    ('http://www.banksecure-login.com', 1),
    ('https://secure.paypal.com.login.verify-account.com', 1),
    ('http://facebook.com', 0),
    ('http://update-login-security-alert.com', 1),
    ('https://github.com', 0),
    ('http://verify-bank-account-free-prize.com', 1),
    ('http://example.com', 0),
    ('https://secure-update-account-verification.com', 1),
    ('https://openai.com', 0)
]

# Insert data into the table
cursor.executemany('INSERT INTO phishing_urls (url, label) VALUES (?, ?)', sample_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database and table created, sample data inserted successfully.")

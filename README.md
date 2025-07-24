Phishing URL Detector

A Streamlit-based machine learning app that detects whether a URL is legitimate or a phishing attempt.

🚀 Features

Upload and analyze URLs to detect phishing.

Uses machine learning models for accurate classification.

SQLite database for storing datasets.

Simple, clean Streamlit UI for live testing and demonstration.

🛠️ Technologies Used

Python (3.10 or above recommended)

Pandas

Scikit-learn

SQLite

Streamlit

Joblib (for model serialization)

📷 App Preview

[Add screenshot here after deployment for visual appeal]

🌐 Live Demo

Access the deployed app here:

👉 Click here to open Phishing URL Detector on Streamlit

🖥️ Running Locally

1️⃣ Clone the repository:

git clone https://github.com/Vedantu77/phishing-url-detector.git
cd phishing-url-detector

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the app:

streamlit run phishing_app.py

📂 Project Structure

phishing-url-detector/
│
├── phishing_app.py                # Main Streamlit app
├── phishing_data.db               # SQLite database with phishing dataset
├── phishing_feature_extraction.py # Feature extraction functions
├── phishing_model.pkl             # Pre-trained ML model
├── phishing_setup_db.py           # Script to set up the database
├── phishing_train_model.py        # Model training script
├── requirements.txt               # Dependencies
└── README.md                      # Project overview

✍️ Author

Vedantu77

🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

⚖️ License

This project is licensed for personal and academic use.

📞 Contact

For queries, feel free to connect via GitHub.

⭐ If you find this project useful, please give it a star on GitHub to support the work!

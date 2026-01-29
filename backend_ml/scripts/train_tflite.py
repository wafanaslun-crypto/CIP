import pandas as pd
from extract_features import extract_features
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("data/phishing_urls.csv")

X = data["url"].apply(extract_features).tolist()
y = data["label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "models/phishing_model.pkl")

print("Model training completed.")

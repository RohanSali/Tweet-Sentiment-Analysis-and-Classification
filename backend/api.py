from fastapi import FastAPI
import pickle
import re

# Initialize app
app = FastAPI()

# Load model
with open("../sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

# Cleaning function
def clean_tweet_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\.\S+', ' ', text)
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Root endpoint
@app.get("/")
def home():
    return {"message": "Tweet Sentiment API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: dict):
    text = data.get("text", "")
    cleaned = clean_tweet_text(text)

    prediction = model.predict([cleaned])[0]

    return {
        "input": text,
        "cleaned": cleaned,
        "prediction": prediction
    }
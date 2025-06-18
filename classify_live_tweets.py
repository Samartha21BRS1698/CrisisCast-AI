# code to classify live tweets as disaster-related or not

import pandas as pd
import pickle

# Load cleaned tweet data
df = pd.read_csv("cleaned_tweets.csv")

# Load model and vectorizer
with open("disaster_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Drop NA and keep only cleaned text
df.dropna(subset=["cleaned_text"], inplace=True)

# Vectorize the cleaned tweets
X = vectorizer.transform(df["cleaned_text"])

# Predict disaster or not
df["predicted_label"] = model.predict(X)
df["prediction_text"] = df["predicted_label"].map({1: "🚨 Disaster", 0: "✅ Not Disaster"})

# Save to new file for dashboard
df.to_csv("classified_tweets.csv", index=False)

print("✅ Live tweets classified and saved to 'classified_tweets.csv'")

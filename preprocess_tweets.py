# code for cleaning and pre-processing the data obtained from tweets
import pandas as pd
import re
import emoji
from nltk.corpus import stopwords

# Load raw tweets
df = pd.read_csv("disaster_tweets.csv")

# Get English stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # remove URLs
    text = re.sub(r"@\w+|#\w+", "", text)  # remove mentions and hashtags
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = emoji.replace_emoji(text, "")  # remove emojis
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    tokens = [word for word in text.split() if word not in stop_words]
    return " ".join(tokens)

# Apply cleaning function
df["cleaned_text"] = df["text"].apply(clean_text)

# Save cleaned dataset
df.to_csv("cleaned_tweets.csv", index=False)

print("✅ Cleaned tweets saved to 'cleaned_tweets.csv'.")

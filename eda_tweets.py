#this is code for performing Exploratory Data Analysis on cleaned dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from datetime import datetime

# Load cleaned data
df = pd.read_csv("cleaned_tweets.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Drop rows with invalid dates
df = df.dropna(subset=["timestamp"])

# Set plot style
sns.set(style="darkgrid")

# === 1. Plot tweet frequency by date ===
df["date"] = df["timestamp"].dt.date
tweet_freq = df.groupby("date").size()

plt.figure(figsize=(10, 5))
tweet_freq.plot(kind="bar")
plt.title("📅 Number of Tweets per Day")
plt.xlabel("Date")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("tweet_freq_by_date.png")
plt.close()

# === 2. Generate WordCloud of common words ===
#all_words = " ".join(df["cleaned_text"])
all_words = " ".join(df["cleaned_text"].dropna().astype(str))

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_words)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("☁️ WordCloud of Cleaned Tweets")
plt.tight_layout()
plt.savefig("tweet_wordcloud.png")
plt.close()

# === 3. (Optional) Print top keywords ===
from collections import Counter

word_list = all_words.split()
common_words = Counter(word_list).most_common(15)
print("🔥 Top 15 Keywords in Disaster Tweets:")
for word, count in common_words:
    print(f"{word}: {count}")

print("\n✅ EDA complete. Plots saved as 'tweet_freq_by_date.png' and 'tweet_wordcloud.png'.")

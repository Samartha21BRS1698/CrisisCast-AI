# this is code for collecting tweets

import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Load Bearer Token from .env
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Set up Twitter API client
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

# Define disaster-related keywords
query = "earthquake OR flood OR landslide OR fire OR cyclone OR hurricane -is:retweet lang:en"

def fetch_disaster_tweets(limit=100):
    tweets_data = []

    try:
        # Fetch recent tweets
        response = client.search_recent_tweets(
            query=query,
            tweet_fields=["created_at", "text", "geo", "author_id"],
            max_results=min(limit, 100)  # Twitter allows max 100 per call
        )

        if response.data:
            for tweet in response.data:
                tweets_data.append({
                    "timestamp": tweet.created_at,
                    "author_id": tweet.author_id,
                    "text": tweet.text,
                    "geo": tweet.geo
                })

            # Save to CSV
            df = pd.DataFrame(tweets_data)
            df.to_csv("disaster_tweets.csv", index=False)
            print(f"✅ {len(tweets_data)} tweets saved to 'disaster_tweets.csv'.")

        else:
            print("⚠️ No tweets found for the given query.")

    except Exception as e:
        print(f"❌ Error fetching tweets: {e}")

if __name__ == "__main__":
    fetch_disaster_tweets(limit=100)

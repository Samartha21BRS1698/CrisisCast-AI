# code for streamlit dashboard

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🌍 CrisisCast AI - Live Disaster Tweet Classifier")

# Load predictions
df = pd.read_csv("classified_tweets.csv")

# Summary stats
disaster_count = df[df["predicted_label"] == 1].shape[0]
non_disaster_count = df[df["predicted_label"] == 0].shape[0]

col1, col2 = st.columns(2)
col1.metric("🚨 Disaster Tweets", disaster_count)
col2.metric("✅ Not Disaster", non_disaster_count)

# Show table
st.subheader("📝 Classified Tweets")
st.dataframe(df[["cleaned_text", "prediction_text"]].rename(columns={
    "cleaned_text": "Tweet", "prediction_text": "Classification"
}))
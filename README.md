
# 🌍 CrisisCast AI

> Real-Time Disaster Tweet Detection and Geo-Analysis System  
> 📅 Built: June 2025  
⚙️Skills:
 • EDA • NLP • Machine Learning • Streamlit • GeoMapping

---

## 🚨 Overview

**CrisisCast AI** is a real-time intelligent system that classifies tweets related to disasters (e.g., earthquakes, floods, wildfires), maps geo-tagged tweets, and visualizes them on an interactive dashboard.

🔍 It uses:
- Machine Learning for binary disaster classification
- NLP techniques for preprocessing and sentiment cues
- Geo-mapping with `folium` for spatial analysis
- Streamlit for a live, interactive web dashboard

---

## 📦 Features

- ✅ **Real-time tweet ingestion & cleaning**
- 🔎 **ML-based disaster classification (TF-IDF + Logistic Regression)**
- 🌍 **Geo-mapping of disaster-tagged tweets**
- 📊 **Live dashboard using Streamlit**
- 💾 **Model & vectorizer saving with `.pkl` files**

---

## 🛠️ Tech Stack

| Layer              | Tools / Libraries                            |
|-------------------|-----------------------------------------------|
| Language           | Python 3.10+                                  |
| Data Processing    | pandas, re, emoji                             |
| Machine Learning   | scikit-learn (Logistic Regression, TF-IDF)    |
| Visualization      | Matplotlib, Seaborn, Folium, Streamlit        |
| Deployment         | Git, GitHub, VS Code, Docker (optional)       |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/Samartha21BRS1698/CrisisCast-AI.git
cd CrisisCast-AI

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run tweet collector
python collect_tweets.py

# Clean the tweet dataset
python preprocess_tweets.py
python eda_tweets.py

# Run ML training
python train_disaster_classifier.py

# Classify live tweets
python classify_live_tweets.py

# Launch dashboard
streamlit run dashboard.py
```

| Map View                        | Dashboard                           |
| -----------------------------   | ----------------------------------- |
| ![alt text](map_view_tweet.png) | ![alt text](streamlit_dashboard.png)

🧠 ML Model Performance
Algorithm: Logistic Regression

Vectorizer: TF-IDF

Accuracy: ~0.85 on test set

Evaluation: Confusion matrix, precision, recall


Confusion Matrix
![alt text](disaster_confusion_matrix.png)

📁 Project Structure


Author: Samartha
🔗 LinkedIn | GitHub

📝 License
 MIT License © 2025 Samartha
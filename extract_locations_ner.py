# this is code for extracting locations bof the tweets using spacy (NLP)
import pandas as pd
import spacy

# Load cleaned tweets
df = pd.read_csv("cleaned_tweets.csv")

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Extract locations using NER
def extract_locations(text):
    doc = nlp(str(text))
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]  # GPE = GeoPolitical Entity (cities, countries)
    return locations

print("🔍 Extracting locations from tweets...")

# Apply extraction
df["locations_extracted"] = df["cleaned_text"].apply(extract_locations)

# Optional: Flatten multiple locations to comma-separated string
df["locations_extracted"] = df["locations_extracted"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)

# Save the results
df.to_csv("tweets_with_locations.csv", index=False)

print("✅ Locations extracted and saved to 'tweets_with_locations.csv'")

# code for mapping tweets with metadata

import pandas as pd
import folium

# Load data
df = pd.read_csv("cleaned_tweets.csv")

# Drop rows with no geo data
geo_df = df.dropna(subset=["geo"])

if geo_df.empty:
    print("⚠️ No geo-tagged tweets found.")
else:
    print(f"✅ Found {len(geo_df)} geo-tagged tweets.")

    # NOTE: The 'geo' column may not contain lat/lon directly. For now we simulate it.
    # This is for testing purposes. Replace with actual lat/lon if available.

    # Simulate lat/lon (replace with actual format if you get real geo-coordinates)
    # Example: Extracting dummy coordinates from string "(lat, lon)"
    """def extract_lat_lon(geo_str):
        try:
            geo_str = str(geo_str).strip("()")
            lat, lon = map(float, geo_str.split(","))
            return lat, lon
        except:
            return None, None"""

    def extract_lat_lon(geo_str):
        try:
            geo_str = str(geo_str).strip("() ")
            parts = geo_str.split(",")
            if len(parts) != 2:
                return None, None
            lat = float(parts[0].strip())
            lon = float(parts[1].strip())
            return lat, lon
        except Exception as e:
            print(f"Error parsing geo string: {geo_str} -> {e}")
            return None, None
    
    geo_df[["lat", "lon"]] = geo_df["geo"].apply(lambda g: pd.Series(extract_lat_lon(g)))
    geo_df = geo_df.dropna(subset=["lat", "lon"])
    
    print(geo_df[["geo", "lat", "lon"]].head())

    # Create a map
    disaster_map = folium.Map(location=[20, 80], zoom_start=3)  # Centered on India by default

    for _, row in geo_df.iterrows():
        folium.CircleMarker(
            location=(row["lat"], row["lon"]),
            radius=5,
            popup=row["cleaned_text"],
            color="red",
            fill=True,
            fill_opacity=0.6
        ).add_to(disaster_map)

    # Save map
    disaster_map.save("geo_mapped_tweets.html")
    print("🗺️ Map saved as 'geo_mapped_tweets.html'. Open in browser to view.")

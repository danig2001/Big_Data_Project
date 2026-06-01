import pandas as pd
import requests

print("Starting data download...")

# Pull weather data from the public REST API
url = "https://archive-api.open-meteo.com/v1/archive?latitude=34.05&longitude=-118.24&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_max,precipitation_sum&timezone=auto"
response = requests.get(url)
weather_data = response.json()

# Convert to Pandas DataFrame
df_weather = pd.DataFrame(weather_data['daily'])

print("Data downloaded! Saving to CSV...")
# Save it to your folder
df_weather.to_csv('raw_weather_data.csv', index=False)
print("Done!")
"""
This script fetches and analyzes weather data for the last 7 days for
Hyderabad, India, using the Open-Meteo API. It adheres to PEP 8 standards.
"""

import requests
import pandas as pd
from datetime import date, timedelta

# Constants for the script
LOCATION_NAME = "Hyderabad, India"
LATITUDE = 17.38
LONGITUDE = 78.48
DAYS_TO_FETCH = 7
# Anomaly is a day with max temp > (30-year avg max temp + this threshold)
ANOMALY_THRESHOLD_CELSIUS = 5


def get_weather_analysis():
    """
    Connects to the Open-Meteo API to retrieve, display, and analyze
    weather data for the last 7 days in Hyderabad.
    """
    print(f"🌦️ Starting weather analysis for {LOCATION_NAME}...")

    # --- 1. Define Date Range ---
    today = date.today()
    start_date = today - timedelta(days=DAYS_TO_FETCH)
    # API data is available up to the previous day
    end_date = today - timedelta(days=1)

    # --- 2. Fetch Recent Weather Data ---
    recent_data = fetch_weather_data(start_date, end_date)
    if recent_data.empty:
        print("Could not retrieve recent weather data. Exiting.")
        return

    # --- 3. Print Weather Records in Tabular Format ---
    print("\n## Weather Records for the Last 7 Days ##")
    print(recent_data.to_string())
    print("-" * 70)

    # --- 4. Find and Print Highest and Lowest Temperatures ---
    find_and_print_extremes(recent_data)
    print("-" * 70)

    # --- 5. Spot and Print Anomalies ---
    spot_and_print_anomalies(recent_data)


def fetch_weather_data(start, end):
    """Fetches daily weather data for a given date range."""
    api_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        f"&start_date={start}&end_date={end}"
        f"&daily=temperature_2m_max,temperature_2m_min,rain_sum,wind_speed_10m_max"
        f"&timezone=auto"
    )
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json().get('daily', {})

        if not data:
            print("Warning: API response did not contain 'daily' data.")
            return pd.DataFrame()

        df = pd.DataFrame(data)
        df['time'] = pd.to_datetime(df['time'])
        df.set_index('time', inplace=True)
        df.rename(columns={
            'temperature_2m_min': 'Min Temp (°C)',
            'temperature_2m_max': 'Max Temp (°C)',
            'rain_sum': 'Rainfall (mm)',
            'wind_speed_10m_max': 'Wind Speed (km/h)'
        }, inplace=True)
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()


def find_and_print_extremes(df):
    """Finds and prints the highest and lowest temperatures from the data."""
    if df.empty:
        return

    highest_temp = df['Max Temp (°C)'].max()
    date_highest = df['Max Temp (°C)'].idxmax().strftime('%Y-%m-%d')
    lowest_temp = df['Min Temp (°C)'].min()
    date_lowest = df['Min Temp (°C)'].idxmin().strftime('%Y-%m-%d')

    print("\n## Temperature Extremes ##")
    print(f"📈 Highest Temperature Recorded: {highest_temp}°C on {date_highest}")
    print(f"📉 Lowest Temperature Recorded:  {lowest_temp}°C on {date_lowest}")


def spot_and_print_anomalies(recent_df):
    """
    Identifies unusually hot days by comparing them to a 30-year
    historical average for the same calendar days.
    """
    print("\n## Anomaly Detection (Unusually Hot Days) ##")
    print(
        f"Checking for days where the max temperature was more than "
        f"{ANOMALY_THRESHOLD_CELSIUS}°C hotter than the 30-year average for that day."
    )

    # Fetch 30-year average (climate normals) for the same calendar days
    start_day_month = recent_df.index[0].strftime('%m-%d')
    end_day_month = recent_df.index[-1].strftime('%m-%d')

    # ✅ THIS URL IS NOW CORRECTED
    climate_api_url = (
        f"https://climate-api.open-meteo.com/v1/climate"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        f"&start_date=2024-{start_day_month}&end_date=2024-{end_day_month}"
        f"&daily=temperature_2m_max"
    )

    try:
        response = requests.get(climate_api_url, timeout=10)
        response.raise_for_status()
        climate_data = response.json().get('daily', {})

        if not climate_data:
            print("Could not fetch climate normals for anomaly detection.")
            return

        climate_df = pd.DataFrame(climate_data)
        # Create a day-of-year key for joining, e.g., '08-25'
        recent_df['day_key'] = recent_df.index.strftime('%m-%d')
        climate_df['day_key'] = pd.to_datetime(climate_df['time']).dt.strftime('%m-%d')
        climate_df.rename(
            columns={'temperature_2m_max': '30-Year Avg Max Temp (°C)'},
            inplace=True
        )

        # Merge recent data with historical averages
        merged_df = pd.merge(
            recent_df,
            climate_df[['day_key', '30-Year Avg Max Temp (°C)']],
            on='day_key'
        )

        # Find anomalies
        merged_df['anomaly'] = (
                merged_df['Max Temp (°C)'] >
                merged_df['30-Year Avg Max Temp (°C)'] + ANOMALY_THRESHOLD_CELSIUS
        )
        anomalies = merged_df[merged_df['anomaly']]

        if not anomalies.empty:
            print("\n🚨 Anomalously Hot Days Found:")
            for index, row in anomalies.iterrows():
                print(
                    f" - {index.strftime('%Y-%m-%d')}: "
                    f"Max was {row['Max Temp (°C)']}°C, "
                    f"which is significantly above the historical "
                    f"average of {row['30-Year Avg Max Temp (°C)']:.1f}°C."
                )
        else:
            print("\n✅ No anomalously hot days detected.")

    except requests.exceptions.RequestException as e:
        print(f"Could not perform anomaly detection due to an error: {e}")


if __name__ == "__main__":
    get_weather_analysis()
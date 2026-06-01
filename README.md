# Big Data Weather Analytics & Predictive Modeling

## Project Title & Description
**Problem:** Understanding how precipitation impacts maximum daily temperatures using historical meteorological data. 
This project builds an end-to-end Big Data workflow to collect, clean, process, and analyze weather data, concluding with a predictive machine learning model and an interactive dashboard.

## Architecture Diagram
* **Data Acquisition:** Public REST API (Open-Meteo) fetching historical weather JSON data.
* **Preprocessing:** Python (`pandas`) used to handle missing values, duplicates, and type conversions.
* **Big Data Processing:** `PySpark` used for large-scale data ingestion and advanced analytics.
* **Analytics & Insights:** PySpark Machine Learning (`LinearRegression`) applied to unstructured/raw data for Predictive Analytics.
* **Visualization:** Power BI used to present final findings.

## Installation & Usage
1. Clone this repository.
2. Install dependencies: `pip install pandas pyspark requests`
3. Run `python 1_data_cleaning.py` to extract from the API and clean the data.
4. Run `python 2_pyspark_analysis.py` to initialize Spark, train the predictive model, and output the dashboard data.

## Key Findings
* **Predictive Insight:** The PySpark Linear Regression model successfully trained on the dataset and determined a negative correlation between rain and temperature.
* **Business Value:** For every 1mm increase in precipitation, the maximum temperature drops by approximately 0.23°C. This allows for predictive modeling of utility/energy usage based solely on rain forecasts.
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

print("Step 1: Pandas Preprocessing & Cleaning...")
# Load the raw data we just downloaded
df = pd.read_csv('raw_weather_data.csv')

# Drop any missing values and duplicate rows (Requirement fulfilled)
df_clean = df.dropna()
df_clean = df_clean.drop_duplicates()

# Save the cleaned data
df_clean.to_csv('cleaned_weather_data.csv', index=False)
print("Data cleaned!")

print("Step 2: Starting PySpark...")
# Initialize Spark Session (Requirement fulfilled)
spark = SparkSession.builder.appName("WeatherAnalytics").getOrCreate()

# Load the cleaned data into PySpark
spark_df = spark.read.csv('cleaned_weather_data.csv', header=True, inferSchema=True)

print("Step 3: Predictive Modeling (Machine Learning)...")
# We will predict the Max Temperature based on how much it Rains (Precipitation)
assembler = VectorAssembler(inputCols=["precipitation_sum"], outputCol="features")
data_prepared = assembler.transform(spark_df)

# Split data into training and testing sets
train_data, test_data = data_prepared.randomSplit([0.8, 0.2])

# Train the Linear Regression model (Requirement fulfilled)
lr = LinearRegression(featuresCol='features', labelCol='temperature_2m_max')
lr_model = lr.fit(train_data)

print("Model trained successfully!")
print(f"Impact of rain on temperature: {lr_model.coefficients[0]}")

print("Step 4: Saving final data for Dashboard...")
# Convert back to Pandas just to save a clean CSV for Power BI/Tableau
final_df = spark_df.toPandas()
final_df.to_csv('final_dashboard_data.csv', index=False)

print("Project coding complete! You are ready for the dashboard.")
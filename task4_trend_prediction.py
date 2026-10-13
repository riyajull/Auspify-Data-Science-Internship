import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# TASK 4: TREND PREDICTION ANALYSIS
# ==========================================

print("=" * 55)
print("TASK 4: NETFLIX TREND PREDICTION")
print("=" * 55)

# Step 1: Load the cleaned dataset
file_path = "outputs/netflix_cleaned.csv"

df = pd.read_csv(file_path)

print("\n1. Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Step 2: Check the release year column
print("\n2. Release year information:")
print(df["release_year"].describe())

# Step 3: Clean release year data
df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
)

df = df.dropna(subset=["release_year"])

df["release_year"] = df["release_year"].astype(int)

# Step 4: Count titles released each year
yearly_counts = (
    df.groupby("release_year")
    .size()
    .sort_index()
)

print("\n3. Titles released per year:")
print(yearly_counts.tail(15))

# Step 5: Save yearly trend chart
os.makedirs("outputs", exist_ok=True)

plt.figure(figsize=(12, 6))

plt.plot(
    yearly_counts.index,
    yearly_counts.values,
    marker="o"
)

plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "outputs/task4_release_year_analysis.png",
    dpi=300
)

plt.show()

print("\nRelease year analysis chart saved!")
print("Location: outputs/task4_release_year_analysis.png")

print("\nStep 3 completed successfully!")

# ==========================================
# STEP 4: FUTURE TREND PREDICTION
# ==========================================

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

print("\n" + "=" * 55)
print("STEP 4: FUTURE TREND PREDICTION")
print("=" * 55)

# Prepare yearly data
trend_df = yearly_counts.reset_index()

trend_df.columns = ["release_year", "total_titles"]

# Use recent years for forecasting
trend_df = trend_df[
    (trend_df["release_year"] >= 2010) &
    (trend_df["release_year"] <= 2021)
].copy()

trend_df = trend_df.sort_values("release_year")

if len(trend_df) < 5:
    raise ValueError(
        "Not enough yearly data to train the forecasting model."
    )

# Features and target
X = trend_df[["release_year"]]
y = trend_df["total_titles"]

# Train on earlier years and test on later years
split_index = int(len(trend_df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Evaluate predictions on test data
test_predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, test_predictions)

print("Mean Absolute Error:", round(mae, 2))

# Forecast the next five years
future_years = np.arange(2022, 2027)

future_X = pd.DataFrame({
    "release_year": future_years
})

future_predictions = model.predict(future_X)

# Predictions represent estimated title counts
future_predictions = np.maximum(
    future_predictions,
    0
)

forecast_df = pd.DataFrame({
    "release_year": future_years,
    "predicted_titles": np.round(
        future_predictions
    ).astype(int)
})

print("\nFuture Trend Forecast:")
print(forecast_df.to_string(index=False))

# Save predictions
forecast_df.to_csv(
    "outputs/netflix_future_trend_predictions.csv",
    index=False
)

print("\nForecast saved successfully!")
print(
    "Location: outputs/netflix_future_trend_predictions.csv"
)

# ==========================================
# STEP 5: FORECAST VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt

print("\n" + "=" * 55)
print("STEP 5: FORECAST VISUALIZATION")
print("=" * 55)

plt.figure(figsize=(12, 6))

# Historical data
plt.plot(
    trend_df["release_year"],
    trend_df["total_titles"],
    marker="o",
    label="Historical Data"
)

# Future predictions
plt.plot(
    forecast_df["release_year"],
    forecast_df["predicted_titles"],
    marker="o",
    linestyle="--",
    label="Predicted Data"
)

plt.title("Netflix Historical and Predicted Content Trends")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "outputs/task4_future_trend.png",
    dpi=300
)

plt.show()

print("\nForecast visualization saved successfully!")
print("Location: outputs/task4_future_trend.png")
print("STEP 5 COMPLETED SUCCESSFULLY!")
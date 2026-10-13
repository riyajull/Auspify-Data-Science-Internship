import pandas as pd
import numpy as np
import os

# Step 1: Load the dataset
df = pd.read_csv("Dataset.csv")

print("=" * 50)
print("TASK 1: DATA CLEANING & PREPROCESSING")
print("=" * 50)

# Step 2: Display dataset information
print("\n1. Original Dataset Shape:")
print(df.shape)

print("\n2. First 5 Rows:")
print(df.head())

print("\n3. Column Names:")
print(df.columns.tolist())

print("\n4. Data Types:")
print(df.dtypes)

# Step 3: Check missing values
print("\n5. Missing Values:")
print(df.isnull().sum())

# Step 4: Check duplicate rows
print("\n6. Duplicate Rows:")
print(df.duplicated().sum())

# Step 5: Remove duplicate rows
df = df.drop_duplicates()

# Step 6: Clean text columns
for column in df.select_dtypes(include=["object", "str"]).columns:
    df[column] = df[column].map(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )

# Step 7: Convert blank strings into missing values
df = df.replace(r"^\s*$", np.nan, regex=True)

print("\n7. Missing Values After Cleaning:")
print(df.isnull().sum())

# Step 8: Convert date_added to datetime

if "date_added" in df.columns:
    df["date_added"] = pd.to_datetime(
        df["date_added"],
        errors="coerce"
    )

print("\nDate Column Data Type:")
if "date_added" in df.columns:
    print(df["date_added"].dtype)

print("\nInvalid Dates:")
if "date_added" in df.columns:
    print(df["date_added"].isna().sum())

# Step 9: Save the cleaned dataset
os.makedirs("outputs", exist_ok=True)

df.to_csv(
    "outputs/netflix_cleaned.csv",
    index=False
)

print("\n8. Final Dataset Shape:")
print(df.shape)

print("\nCleaned dataset saved successfully!")
print("Location: outputs/netflix_cleaned.csv")
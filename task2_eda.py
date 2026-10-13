import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# TASK 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

# Step 1: Load the cleaned dataset
df = pd.read_csv("outputs/netflix_cleaned.csv")

print("=" * 55)
print("TASK 2: EXPLORATORY DATA ANALYSIS")
print("=" * 55)

# Step 2: Explore dataset structure
print("\n1. Dataset Shape:")
print(df.shape)

print("\n2. Dataset Information:")
df.info()

print("\n3. Statistical Summary:")
print(df.describe(include="all").T)

print("\n4. Missing Values:")
print(df.isnull().sum())

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Set chart style
sns.set_theme(style="whitegrid")

# ==========================================
# ANALYSIS 1: CONTENT DISTRIBUTION BY TYPE
# ==========================================

print("\n5. Content Distribution by Type:")
print(df["type"].value_counts())

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Content Distribution")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig(
    "outputs/content_distribution.png",
    dpi=300
)

plt.show()

# ==========================================
# ANALYSIS 2: TOP 10 COUNTRIES
# ==========================================

print("\n6. Top 10 Countries by Content:")

countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .str.strip()
)

top_countries = countries.value_counts().head(10)

print(top_countries)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    "outputs/top_10_countries.png",
    dpi=300
)

plt.show()

# ==========================================
# ANALYSIS 3: CONTENT RELEASE BY YEAR
# ==========================================

print("\n7. Content Released by Year:")

yearly_content = df["release_year"].value_counts().sort_index()

print("\nMost Recent Release Years:")
print(yearly_content.tail(10))

plt.figure(figsize=(12, 6))

yearly_content.plot(kind="line")

plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig(
    "outputs/release_year_trend.png",
    dpi=300
)

plt.show()

# ==========================================
# ANALYSIS 4: TOP CONTENT CATEGORIES
# ==========================================

print("\n8. Top 10 Content Categories:")

categories = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .str.strip()
)

top_categories = categories.value_counts().head(10)

print(top_categories)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_categories.values,
    y=top_categories.index
)

plt.title("Top 10 Netflix Content Categories")
plt.xlabel("Number of Titles")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig(
    "outputs/top_10_categories.png",
    dpi=300
)

plt.show()

# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n" + "=" * 55)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 55)

print("\nTotal Titles:", len(df))

print("\nContent Type Distribution:")
print(df["type"].value_counts())

print("\nCharts saved in the outputs folder:")
print("- content_distribution.png")
print("- top_10_countries.png")
print("- release_year_trend.png")
print("- top_10_categories.png")
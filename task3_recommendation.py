import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# TASK 3: RECOMMENDATION SYSTEM ANALYSIS
# ==========================================

print("=" * 60)
print("NETFLIX CONTENT RECOMMENDATION SYSTEM")
print("=" * 60)

# Step 1: Load the cleaned dataset
file_path = "outputs/netflix_cleaned.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"Dataset not found: {file_path}"
    )

df = pd.read_csv(file_path)

print("\n1. Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Step 2: Select relevant content features
feature_columns = [
    "title",
    "type",
    "director",
    "cast",
    "listed_in",
    "description"
]

# Use only columns available in the dataset
available_columns = [
    col for col in feature_columns
    if col in df.columns
]

print("\n2. Available recommendation features:")
print(available_columns)

# Fill missing values in text features
for column in available_columns:
    df[column] = df[column].fillna("").astype(str)

# Keep rows with valid titles
df = df[df["title"].str.strip() != ""].copy()

# Reset index for consistent similarity calculations
df.reset_index(drop=True, inplace=True)

# Step 3: Combine relevant features
text_columns = [
    col for col in available_columns
    if col != "title"
]

df["combined_features"] = df[text_columns].agg(
    " ".join,
    axis=1
)

print("\n3. Content features combined successfully!")

# Step 4: Text preprocessing and TF-IDF
vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True
)

tfidf_matrix = vectorizer.fit_transform(
    df["combined_features"]
)

print("TF-IDF matrix shape:", tfidf_matrix.shape)

# Step 5: Calculate content similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

print("\n4. Similarity matrix created successfully!")
print("Similarity matrix shape:", similarity_matrix.shape)


# ==========================================
# RECOMMENDATION FUNCTION
# ==========================================

def recommend_titles(title, number_of_recommendations=5):

    matches = df.index[
        df["title"].str.casefold() == title.casefold()
    ].tolist()

    if not matches:
        print(f"\nTitle not found: {title}")
        print("Please enter a title from the dataset.")
        return pd.DataFrame()

    # Use the first matching title
    title_index = matches[0]

    similarity_scores = list(
        enumerate(similarity_matrix[title_index])
    )

    # Sort by similarity, highest first
    similarity_scores.sort(
        key=lambda item: item[1],
        reverse=True
    )

    # Exclude the selected title itself
    recommendations = []

    for index, score in similarity_scores:
        if index == title_index:
            continue

        recommendations.append((index, score))

        if len(recommendations) == number_of_recommendations:
            break

    result_indices = [
        index for index, score in recommendations
    ]

    result = df.loc[
        result_indices,
        ["title", "type"] +
        (["listed_in"] if "listed_in" in df.columns else [])
    ].copy()

    result["similarity_score"] = [
        round(score, 3)
        for index, score in recommendations
    ]

    return result


# ==========================================
# STEP 6: GENERATE RECOMMENDATIONS
# ==========================================

test_title = "The Matrix"

print(f"\n5. Recommendations for '{test_title}':")

recommendations = recommend_titles(test_title)

if not recommendations.empty:
    print(recommendations.to_string(index=False))

# ==========================================
# STEP 7: SAVE RECOMMENDATIONS
# ==========================================

os.makedirs("outputs", exist_ok=True)

if not recommendations.empty:
    output_path = "outputs/netflix_recommendations.csv"

    recommendations.to_csv(
        output_path,
        index=False
    )

    print("\nRecommendations saved successfully!")
    print("Location:", output_path)
else:
    print(
        "\nNo recommendations were saved. "
        "Check whether the selected title exists."
    )

# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("RECOMMENDATION SYSTEM EXECUTION COMPLETED")
print("=" * 60)

# ==========================================
# STEP 8: RECOMMENDATION QUALITY EVALUATION
# ==========================================

print("\n" + "=" * 60)
print("RECOMMENDATION QUALITY EVALUATION")
print("=" * 60)

# Calculate average similarity of recommended titles
if not recommendations.empty:

    average_similarity = recommendations[
        "similarity_score"
    ].mean()

    print("\nTotal recommendations generated:",
          len(recommendations))

    print("Average similarity score:",
          round(average_similarity, 3))

    print("\nEvaluation Summary:")

    if average_similarity >= 0.70:
        print("Recommended titles have high feature similarity.")
    elif average_similarity >= 0.40:
        print("Recommended titles have moderate feature similarity.")
    else:
        print("Recommended titles have low feature similarity.")

    print(
        "\nNote: Similarity measures feature overlap, "
        "not actual user satisfaction."
    )

else:
    print("Evaluation could not be performed.")
    print("No recommendations available.")
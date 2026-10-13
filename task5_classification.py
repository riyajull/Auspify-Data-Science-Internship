# Task 5: Machine Learning Classification Model
# Auspify Technologies - Data Science Internship

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay
)

# --------------------------------------------------
# Step 1: Load Dataset
# --------------------------------------------------

DATA_PATH = "outputs/netflix_cleaned.csv"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)
print("\nAvailable columns:")
print(df.columns.tolist())

# --------------------------------------------------
# Step 2: Prepare Target and Features
# --------------------------------------------------

# Target column: type (Movie or TV Show)
df = df.dropna(subset=["type"]).copy()

# Select features available in the dataset
candidate_features = [
    "listed_in",
    "release_year",
    "rating",
    "duration",
    "country"
]

features = [col for col in candidate_features if col in df.columns]

# Verification: Check model without duration and rating
verification_features = [
    col for col in features
    if col not in ["duration", "rating"]
]

print("\nFeatures used in verification:", verification_features)

if not features:
    raise ValueError("No suitable feature columns found.")

X = df[features].copy()
y = df["type"].copy()

# Convert text/categorical values to consistent format
for col in X.select_dtypes(include=["object", "str"]).columns:
    X[col] = X[col].fillna("Unknown").astype(str).str.strip()
    X[col] = X[col].replace("", "Unknown")

# Convert numeric columns
for col in X.columns:
    if col == "release_year":
        X[col] = pd.to_numeric(X[col], errors="coerce")

print("\nSelected features:", features)
print("\nTarget distribution:")
print(y.value_counts())

# --------------------------------------------------
# Step 3: Split Dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# --------------------------------------------------
# Step 4: Build Preprocessing Pipeline
# --------------------------------------------------

text_features = [
    col for col in ["listed_in", "country"]
    if col in features
]

categorical_features = [
    col for col in ["rating", "duration"]
    if col in features
]

numeric_features = [
    col for col in ["release_year"]
    if col in features
]

transformers = []

for col in text_features:
    transformers.append(
        (
            f"text_{col}",
            TfidfVectorizer(max_features=3000),
            col
        )
    )

if categorical_features:
    transformers.append(
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    )

if numeric_features:
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    transformers.append(
        (
            "numeric",
            numeric_pipeline,
            numeric_features
        )
    )

preprocessor = ColumnTransformer(
    transformers=transformers,
    remainder="drop"
)

# --------------------------------------------------
# Step 5: Train Classification Model
# --------------------------------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42
            )
        )
    ]
)

print("\nTraining the classification model...")

model.fit(X_train, y_train)

print("Model training completed successfully!")

# --------------------------------------------------
# Step 6: Evaluate Model
# --------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("CLASSIFICATION MODEL RESULTS")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Accuracy Percentage: {accuracy * 100:.2f}%")

print("\nClassification Report:")
report = classification_report(
    y_test,
    y_pred,
    zero_division=0
)

print(report)

# --------------------------------------------------
# Step 7: Save Evaluation Results
# --------------------------------------------------

with open(
    os.path.join(OUTPUT_DIR, "task5_classification_report.txt"),
    "w",
    encoding="utf-8"
) as file:
    file.write("Netflix Content Classification Report\n")
    file.write("=" * 40 + "\n")
    file.write(f"Features used: {features}\n")
    file.write(f"Accuracy: {accuracy:.4f}\n\n")
    file.write(report)

# --------------------------------------------------
# Step 8: Create Confusion Matrix
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(7, 5))

ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    ax=ax,
    cmap="Blues",
    colorbar=False
)

ax.set_title("Netflix Content Classification")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "task5_confusion_matrix.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Step 9: Save Predictions
# --------------------------------------------------

predictions = X_test.copy()
predictions["actual_type"] = y_test
predictions["predicted_type"] = y_pred

predictions.to_csv(
    os.path.join(OUTPUT_DIR, "task5_classification_predictions.csv"),
    index=False
)

# --------------------------------------------------
# Final Summary
# --------------------------------------------------

print("\nFiles saved successfully in the outputs folder:")
print("- task5_classification_report.txt")
print("- task5_confusion_matrix.png")
print("- task5_classification_predictions.csv")

print("\nTask 5 completed successfully!")

# --------------------------------------------------
# Verification: Test model without duration and rating
# --------------------------------------------------

print("\n" + "=" * 50)
print("MODEL VERIFICATION")
print("=" * 50)

verification_features = [
    col for col in features
    if col not in ["duration", "rating"]
]

X_verify = df[verification_features].copy()
y_verify = df["type"].copy()

for col in X_verify.select_dtypes(include=["object", "str"]).columns:
    X_verify[col] = (
        X_verify[col]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .replace("", "Unknown")
    )

verify_text_features = [
    col for col in ["listed_in", "country"]
    if col in verification_features
]

verify_numeric_features = [
    col for col in ["release_year"]
    if col in verification_features
]

verify_transformers = []

for col in verify_text_features:
    verify_transformers.append(
        (
            f"text_{col}",
            TfidfVectorizer(max_features=3000),
            col
        )
    )

if verify_numeric_features:
    verify_transformers.append(
        (
            "numeric",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]),
            verify_numeric_features
        )
    )

verify_preprocessor = ColumnTransformer(
    transformers=verify_transformers,
    remainder="drop"
)

verify_model = Pipeline([
    ("preprocessor", verify_preprocessor),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

X_train_v, X_test_v, y_train_v, y_test_v = train_test_split(
    X_verify,
    y_verify,
    test_size=0.20,
    random_state=42,
    stratify=y_verify
)

verify_model.fit(X_train_v, y_train_v)

verify_predictions = verify_model.predict(X_test_v)

verify_accuracy = accuracy_score(y_test_v, verify_predictions)

print("Original model accuracy:", round(accuracy * 100, 2), "%")
print("Verification model accuracy:", round(verify_accuracy * 100, 2), "%")

print("\nVerification classification report:")
print(classification_report(
    y_test_v,
    verify_predictions,
    zero_division=0
))

print("\nVerification completed!")
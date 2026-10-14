# 📊 Netflix Data Science Projects

### Auspify Technologies — Data Science Internship

A practical collection of six Python-based Data Science projects completed as part of the **4-Week Data Science Internship Program at Auspify Technologies**.

This repository explores the complete Data Science workflow using a Netflix titles dataset, from data cleaning and exploratory analysis to recommendation systems, forecasting, machine learning classification, and an interactive Streamlit dashboard.

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Science-blue?logo=python" alt="Python Data Science">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-FF4B4B?logo=streamlit" alt="Streamlit">
</p>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Project Highlights](#-project-highlights)
- [Project Structure](#-project-structure)
- [Internship Tasks](#-internship-tasks)
- [Dashboard Preview](#-dashboard-preview)
- [Technologies Used](#-technologies-used)
- [Installation and Setup](#-installation-and-setup)
- [Running the Projects](#-running-the-projects)
- [Screenshots](#-screenshots)
- [Learning Outcomes](#-learning-outcomes)
- [Limitations and Considerations](#-limitations-and-considerations)
- [About the Internship](#-about-the-internship)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Project Overview

The objective of this project is to apply practical Data Science techniques to a Netflix titles dataset.

Each task focuses on a different stage of the Data Science workflow, including data preprocessing, statistical exploration, content similarity, trend forecasting, classification, and analytical visualization.

The projects are implemented as standalone Python scripts, allowing each task to be executed and explored independently.

### Key Objectives

- Prepare raw data for reliable analysis.
- Discover patterns and trends through exploratory data analysis.
- Recommend similar titles using content features.
- Analyze historical trends and explore future forecasts.
- Train and evaluate machine learning classification models.
- Present analytical information through an interactive dashboard.

---

## ✨ Project Highlights

- **Data Preparation:** Identify missing values, duplicate records, and data quality issues.
- **Exploratory Analysis:** Explore Netflix content distribution, countries, ratings, and release-year patterns.
- **Recommendation System:** Use text features and similarity calculations to identify related titles.
- **Trend Forecasting:** Analyze historical trends and generate regression-based forecasts.
- **Classification:** Train and evaluate classification models using selected dataset features.
- **Interactive Dashboard:** Present key metrics and visualizations using Streamlit.

---

## 📂 Project Structure

```text
Auspify-Data-Science-Internship/
│
├── Dataset.csv
├── README.md
├── README_backup.md
├── LICENSE
│
├── task1_data_cleaning.py
├── task2_eda.py
├── task3_recommendation.py
├── task4_trend_prediction.py
├── task5_classification.py
├── task6_dashboard.py
├── task6_dashboard_backup.py
│
├── outputs/
│
└── screenshots/
    ├── Task1_Data_Cleaning/
    ├── Task2_EDA/
    ├── Task3_Recommendation/
    ├── Task4_Trend_Prediction/
    ├── Task5_Classification/
    └── Task6_Dashboard/
```

**Note:** This structure represents the current project organization. The contents of the `outputs/` directory may vary depending on the generated files.

---

## 🧩 Internship Tasks

### Task 1 — Data Cleaning and Preprocessing

**Difficulty:** Easy

Prepare the Netflix dataset for analysis by examining data quality and transforming relevant columns.

**Key Activities**
- Inspect dataset structure and data types.
- Identify missing values and duplicate records.
- Handle missing data.
- Convert relevant columns into usable formats.
- Prepare data for subsequent analysis.

**Technologies:** Python, Pandas, NumPy

**Screenshots:** [`screenshots/Task1_Data_Cleaning/`](screenshots/Task1_Data_Cleaning/)

---

### Task 2 — Exploratory Data Analysis (EDA)

**Difficulty:** Easy

Explore the Netflix catalogue to understand its composition and identify meaningful patterns.

**Key Activities**
- Examine dataset statistics.
- Compare movies and TV shows.
- Explore country and rating distributions.
- Analyze release-year patterns and content categories.
- Visualize important findings.

**Technologies:** Pandas, Matplotlib, Seaborn

**Screenshots:** [`screenshots/Task2_EDA/`](screenshots/Task2_EDA/)

---

### Task 3 — Content-Based Recommendation System

**Difficulty:** Medium

Develop a recommendation approach that identifies similar Netflix titles using available textual features.

**Key Activities**
- Prepare relevant text features.
- Convert textual information into numerical representations.
- Calculate content similarity.
- Rank similar titles.
- Inspect sample recommendations.

**Technologies:** Python, Scikit-learn, TF-IDF, Cosine Similarity

**Screenshots:** [`screenshots/Task3_Recommendation/`](screenshots/Task3_Recommendation/)

---

### Task 4 — Trend Prediction Analysis

**Difficulty:** Medium

Analyze historical release-year patterns and explore a simple forecasting approach.

**Key Activities**
- Prepare release-year data.
- Analyze historical content trends.
- Fit a regression-based forecasting model.
- Calculate prediction errors using an evaluation metric.
- Visualize historical values and forecasts.

**Technologies:** Pandas, NumPy, Matplotlib, Scikit-learn

**Important:** Regression-based forecasts are exploratory estimates. They should not be interpreted as guaranteed predictions of future Netflix releases.

**Screenshots:** [`screenshots/Task4_Trend_Prediction/`](screenshots/Task4_Trend_Prediction/)

---

### Task 5 — Machine Learning Classification

**Difficulty:** Advanced

Build a machine learning classification model to predict whether a Netflix title is a Movie or TV Show using selected dataset features.

**Key Activities**

- Prepare model features and target labels.
- Handle missing and categorical values through preprocessing pipelines.
- Split the dataset into training and testing sets.
- Train a Logistic Regression classifier.
- Evaluate model performance using accuracy, classification reports, and a confusion matrix.
- Perform 5-fold stratified cross-validation.
- Compare results with an additional experiment that excludes the `listed_in` feature.

**Technologies:** Python, Pandas, Scikit-learn, Matplotlib

**Model Configuration**

- **Target:** `type` (Movie or TV Show)
- **Original features:** `listed_in`, `release_year`, `rating`, `duration`, `country`
- **Algorithm:** Logistic Regression
- **Train-test split:** 80% training, 20% testing
- **Dataset size:** 8,790 rows

**Results**

| Evaluation | Accuracy |
|---|---:|
| Original model — test set | 99.94% |
| Original model — 5-fold cross-validation mean | 100.00% |
| Model without `listed_in` — test set | 99.89% |
| Model without `listed_in` — 5-fold cross-validation mean | 99.82% |

The original model achieved 99.94% accuracy on the held-out test set. An additional experiment without `listed_in` achieved 99.89% test accuracy, indicating that the remaining features are also highly informative for distinguishing Movies from TV Shows.

**Generated Outputs**

- [Classification Report](outputs/task5_classification_report.txt)
- [Confusion Matrix](outputs/task5_confusion_matrix.png)
- [Classification Predictions](outputs/task5_classification_predictions.csv)

**Evaluation Considerations**

The reported metrics were obtained using splits of the same dataset. The cross-validation results are based on the training set and do not constitute independent external validation. The very high scores should be interpreted in the context of the dataset's feature patterns; performance on unseen external data has not been established.

**Screenshots:** [`screenshots/Task5_Classification/`](screenshots/Task5_Classification/)

---

### Task 6 — Data Science Business Insights Dashboard

**Difficulty:** Advanced

Create an interactive dashboard that presents Netflix dataset metrics, trends, and visual insights.

**Key Activities**
- Present key analytical metrics.
- Explore content distributions.
- Visualize geographical and rating patterns.
- Display relevant business insights.
- Organize visualizations in an interactive interface.

**Technologies:** Python, Streamlit, Pandas, Plotly

**Screenshots:** [`screenshots/Task6_Dashboard/`](screenshots/Task6_Dashboard/)

---

## 📊 Dashboard Preview

The dashboard brings together analytical visualizations and insights from the Netflix dataset.

### Dashboard Overview

![Netflix Dashboard Overview](screenshots/Task6_Dashboard/Dashboard%20Overview.png)

### Business Insights

![Netflix Business Insights](screenshots/Task6_Dashboard/Business%20Insights.png)

*If an image does not render, check its filename and path in the repository.*

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning, text vectorization, and similarity calculations |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive charts |

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- Git
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/riyajull/Auspify-Data-Science-Internship.git
```

### 2. Navigate to the Project Directory

```bash
cd Auspify-Data-Science-Internship
```

### 3. Create a Virtual Environment

**Windows — PowerShell**

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can activate the environment using Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 5. Install Dependencies

After creating the project's `requirements.txt` file, install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

If a script reports a missing package, verify its imports and update the dependency list accordingly.

---

## ▶️ Running the Projects

Run the commands from the project root directory.

Ensure that `Dataset.csv` is available at the location expected by the relevant script.

### Task 1 — Data Cleaning

```bash
python task1_data_cleaning.py
```

### Task 2 — Exploratory Data Analysis

```bash
python task2_eda.py
```

### Task 3 — Recommendation System

```bash
python task3_recommendation.py
```

### Task 4 — Trend Prediction

```bash
python task4_trend_prediction.py
```

### Task 5 — Classification Model

```bash
python task5_classification.py
```

### Task 6 — Interactive Dashboard

Launch the dashboard with Streamlit:

```bash
streamlit run task6_dashboard.py
```

The dashboard is generally available at:

```text
http://localhost:8501
```

**Important:** Run the dashboard using `streamlit run task6_dashboard.py`, not `python task6_dashboard.py`.

---

## 📸 Screenshots

Screenshots for each task are organized into dedicated folders.

| Task | Screenshot Folder |
|---|---|
| Task 1 — Data Cleaning | [`Task1_Data_Cleaning`](screenshots/Task1_Data_Cleaning/) |
| Task 2 — EDA | [`Task2_EDA`](screenshots/Task2_EDA/) |
| Task 3 — Recommendation | [`Task3_Recommendation`](screenshots/Task3_Recommendation/) |
| Task 4 — Trend Prediction | [`Task4_Trend_Prediction`](screenshots/Task4_Trend_Prediction/) |
| Task 5 — Classification | [`Task5_Classification`](screenshots/Task5_Classification/) |
| Task 6 — Dashboard | [`Task6_Dashboard`](screenshots/Task6_Dashboard/) |

These screenshots document selected outputs and visualizations from the implementation.

---

## 🚀 Live Dashboard

Explore the deployed Streamlit dashboard:

**[Open Netflix Data Science Dashboard](https://auspify-data-science-internship-58qojsenn592eyhjbut46g.streamlit.app/)**

The deployment returned HTTP status `200` during a connectivity check. This confirms an HTTP response, not complete verification of every dashboard feature.

---

## 🧪 Load Testing

Load-testing scripts and recorded results are available below:

- [Load Test Results](LOAD_TEST_RESULTS.md)
- [Standard Load Test Script](load_test.js)
- [Cloud Smoke Test Script](cloud_smoke_test.js)

The recorded tests cover HTTP endpoints. They do not establish performance for every interactive dashboard feature or guarantee behavior under all production traffic levels.

---
## 📚 Learning Outcomes
This internship project provides practical experience with:

- Data cleaning and preprocessing using Pandas.
- Exploratory data analysis and visualization.
- Text vectorization and content similarity.
- Regression-based trend forecasting.
- Classification model training and evaluation.
- Interactive dashboard development.
- Python project organization and documentation.
- Version control using Git and GitHub.

---

## ⚠️ Limitations and Considerations

- Results depend on the quality and coverage of the available dataset.
- Recommendations depend on the text features and similarity method used.
- Forecasts are exploratory estimates and may not represent future content growth accurately.
- Classification performance must be interpreted alongside the target definition, feature selection, and validation approach.
- Dashboard insights describe the available dataset and should not automatically be treated as current Netflix business statistics.

---

## 🎓 About the Internship

**Organization:** Auspify Technologies  
**Program:** Data Science Internship  
**Duration:** 4 Weeks  
**Format:** Remote

The internship focuses on practical learning, project-based experience, and portfolio development.

---

## 👨‍💻 Author

**GitHub:** [riyajull](https://github.com/riyajull)

**Project Repository:** [Auspify Data Science Internship](https://github.com/riyajull/Auspify-Data-Science-Internship)

---

## 📄 License

See the [`LICENSE`](LICENSE) file for licensing information.

---

## 🔖 Topics

`Python` · `Data Science` · `Pandas` · `Machine Learning` · `EDA` · `Netflix Dataset` · `Recommendation Systems` · `Forecasting` · `Streamlit` · `Data Visualization`

---

**Learn • Build • Grow**

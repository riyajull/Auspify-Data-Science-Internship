# Auspify Technologies — Data Science Internship

## Netflix Data Analysis, Machine Learning & Business Insights Dashboard

A collection of six practical Data Science projects developed using Python and the Netflix dataset as part of the **Auspify Technologies Data Science Internship Program**.

The project covers data cleaning, exploratory data analysis, content-based recommendation, trend prediction, machine learning classification, and an interactive business insights dashboard.

The objective is to apply data science concepts to a real-world dataset, generate meaningful insights, and build practical project experience.

---

## About Auspify Technologies

Auspify Technologies is a technology and training platform focused on helping students develop industry-relevant skills through practical learning, hands-on tasks, and project-based experience.

**Internship Program:** Data Science Internship  
**Program Duration:** 4 Weeks  
**Learning Approach:** Practical Projects and Hands-On Learning

---

## Project Objectives

- Clean and preprocess the Netflix dataset.
- Explore content distribution and identify meaningful patterns.
- Develop a content-based recommendation system.
- Analyze historical release-year trends and generate baseline forecasts.
- Build and evaluate a machine learning classification model.
- Develop an interactive dashboard for data exploration and business insights.
- Practice data visualization, model evaluation, and professional project organization.

---

## Technologies Used

| Technology / Library | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations, where required |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization, where used |
| Scikit-learn | Machine learning, TF-IDF, similarity calculations, and model evaluation |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive charts and visualizations |

---

# Internship Tasks

## Task 1 — Data Cleaning & Preprocessing

**Difficulty:** Easy  
**Python File:** `task1_data_cleaning.py`

### Description

This task prepares the Netflix dataset for further analysis by inspecting its structure, checking data quality, transforming columns, and saving the processed dataset.

### Objectives

- Load the dataset using Pandas.
- Inspect column names, data types, and dataset structure.
- Check for missing values and duplicate records.
- Handle data inconsistencies where required.
- Convert date-related information into an appropriate format.
- Save the cleaned dataset for subsequent tasks.

### Libraries Used

- **Pandas:** Loading, inspecting, cleaning, and transforming the dataset.
- **NumPy:** Numerical operations, if used in the implementation.

### Output

- `outputs/netflix_cleaned.csv`

### Run Command

```bash
python task1_data_cleaning.py
```

---

## Task 2 — Exploratory Data Analysis (EDA)

**Difficulty:** Easy  
**Python File:** `task2_eda.py`

### Description

This task explores the Netflix dataset to understand content distribution, country representation, categories, and release-year patterns.

### Objectives

- Examine dataset structure and summary statistics.
- Compare the distribution of Movies and TV Shows.
- Analyze the countries represented in the dataset.
- Explore content categories.
- Study release-year trends.
- Generate visualizations to communicate findings.

### Libraries Used

- **Pandas:** Data analysis and aggregation.
- **Matplotlib:** Creating charts and visualizations.
- **Seaborn:** Statistical visualization, if used in the implementation.

### Outputs

- `outputs/content_distribution.png`
- `outputs/top_10_categories.png`
- `outputs/top_10_countries.png`
- `outputs/release_year_trend.png`

### Run Command

```bash
python task2_eda.py
```

---

## Task 3 — Content-Based Recommendation System

**Difficulty:** Medium  
**Python File:** `task3_recommendation.py`

### Description

This task implements a basic content-based recommendation system that identifies Netflix titles with similar content features.

### Objectives

- Extract relevant information from Netflix titles.
- Combine available features such as title, type, director, and categories.
- Convert text features into numerical representations using TF-IDF.
- Calculate content similarity using cosine similarity.
- Generate recommendations for a selected title.

### Libraries Used

- **Pandas:** Loading data and organizing recommendation results.
- **Scikit-learn:** TF-IDF vectorization and cosine similarity calculations.

### Output

- `outputs/netflix_recommendations.csv`

### Run Command

```bash
python task3_recommendation.py
```

### Note

Recommendations are generated from similarities between available content features. A high similarity score does not necessarily indicate user preference or satisfaction.

---

## Task 4 — Trend Prediction Analysis

**Difficulty:** Medium  
**Python File:** `task4_trend_prediction.py`

### Description

This task analyzes the historical release years of Netflix titles and uses a basic forecasting model to estimate trends.

### Objectives

- Prepare and analyze release-year data.
- Visualize historical content trends.
- Train a baseline forecasting model.
- Generate estimates for future years.
- Evaluate model predictions using Mean Absolute Error (MAE).
- Visualize historical trends and forecast results.

### Libraries Used

- **Pandas:** Data preparation and tabular analysis.
- **Matplotlib:** Visualizing historical trends and predictions.
- **Scikit-learn:** Building and evaluating the Linear Regression model.

### Outputs

- `outputs/task4_release_year_analysis.png`
- `outputs/netflix_future_trend_predictions.csv`
- `outputs/task4_future_trend.png`

### Run Command

```bash
python task4_trend_prediction.py
```

### Note

The forecasts are baseline model estimates based on historical release-year data. They should not be interpreted as actual future Netflix releases or Netflix's future content acquisition plans.

---

## Task 5 — Machine Learning Classification Model

**Difficulty:** Advanced  
**Python File:** `task5_classification.py`

### Description

This task applies machine learning classification to predict the content type of a Netflix title using selected dataset features.

The model is designed to classify titles into categories such as **Movie** and **TV Show**.

### Objectives

- Select relevant dataset features.
- Prepare categorical and numerical features.
- Split data into training and testing sets.
- Train a classification model.
- Generate predictions for the test data.
- Evaluate model performance.
- Save evaluation results and predictions.

### Libraries Used

- **Pandas:** Data preparation and handling predictions.
- **Scikit-learn:** Feature preprocessing, model training, data splitting, and performance evaluation.
- **Matplotlib:** Confusion matrix visualization, if used in the implementation.

### Outputs

- `outputs/task5_classification_report.txt`
- `outputs/task5_confusion_matrix.png`
- `outputs/task5_classification_predictions.csv`

### Run Command

```bash
python task5_classification.py
```

### Note

Classification results depend on the selected features, preprocessing, data split, and evaluation method. Reported performance should be interpreted in the context of the dataset and the features used.

---

## Task 6 — Data Science Business Insights Dashboard

**Difficulty:** Advanced  
**Python File:** `task6_dashboard.py`

### Description

This task brings data analysis and visualization together in an interactive dashboard built with Streamlit and Plotly.

The dashboard provides an accessible way to explore Netflix content and review data-driven insights.

### Objectives

- Load the cleaned Netflix dataset.
- Display key dataset metrics.
- Explore content using interactive filters.
- Visualize important data patterns.
- Present business-oriented insights.
- Preview and download dataset information.

### Libraries Used

- **Pandas:** Data processing, filtering, and aggregation.
- **Streamlit:** Dashboard interface and interactive controls.
- **Plotly:** Interactive charts and visualizations.

### Dashboard Features

- Netflix-inspired dashboard design.
- Key performance indicator (KPI) cards.
- Interactive sidebar filters.
- Content distribution visualizations.
- Country and category analysis.
- Release-year trend analysis.
- Business insights section.
- Dataset preview and download functionality.
- Developer credit and project footer.

### Run Command

```bash
python -m streamlit run task6_dashboard.py
```

After running the command, Streamlit will provide a local URL in the terminal. Open that URL in your browser to use the dashboard.

### Screenshots

Dashboard screenshots are stored in the `screenshots/` directory.

Suggested screenshots:

- `screenshots/task6_dashboard_overview.png`
- `screenshots/task6_charts.png`
- `screenshots/task6_business_insights.png`
- `screenshots/task6_footer.png`

Screenshots can be added to this README using Markdown:

```markdown
![Dashboard Overview](screenshots/task6_dashboard_overview.png)
```

---

# Project Structure

```text
Auspify_Data_Science_Internship/
│
├── Dataset.csv
├── README.md
│
├── task1_data_cleaning.py
├── task2_eda.py
├── task3_recommendation.py
├── task4_trend_prediction.py
├── task5_classification.py
├── task6_dashboard.py
│
├── outputs/
│   ├── netflix_cleaned.csv
│   ├── netflix_recommendations.csv
│   ├── netflix_future_trend_predictions.csv
│   ├── content_distribution.png
│   ├── top_10_categories.png
│   ├── top_10_countries.png
│   ├── release_year_trend.png
│   ├── task4_release_year_analysis.png
│   ├── task4_future_trend.png
│   ├── task5_classification_report.txt
│   ├── task5_confusion_matrix.png
│   └── task5_classification_predictions.csv
│
└── screenshots/
    ├── task6_dashboard_overview.png
    ├── task6_charts.png
    ├── task6_business_insights.png
    └── task6_footer.png
```

**Note:** The structure above shows the main project files and expected outputs. Actual generated files may vary depending on which scripts have been run.

---

# Installation & Setup

## 1. Prerequisites

Make sure the following are installed:

- Python
- PyCharm or another Python IDE
- Required Python libraries

## 2. Open the Project

Open the `Auspify_Data_Science_Internship` project folder in PyCharm.

Make sure `Dataset.csv` is present in the project root directory.

## 3. Install Required Libraries

Open the PyCharm terminal and run:

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn streamlit plotly
```

This installs the libraries used across the project's tasks. You do not need to install the same library separately for every task if it is already installed in your active Python environment.

## 4. Run Individual Tasks

Run the scripts from the project root directory:

```bash
python task1_data_cleaning.py
python task2_eda.py
python task3_recommendation.py
python task4_trend_prediction.py
python task5_classification.py
```

Task 6 is an interactive Streamlit dashboard. Start it separately:

```bash
python -m streamlit run task6_dashboard.py
```

## 5. Check Generated Outputs

Generated datasets, reports, and charts are saved in the `outputs/` directory, according to the output paths configured in each script.

---

# Learning Outcomes

Through these projects, I gained practical experience in:

- Data cleaning and preprocessing.
- Handling structured datasets with Pandas.
- Exploratory Data Analysis (EDA).
- Data visualization and interpretation.
- Text preprocessing and TF-IDF vectorization.
- Content-based recommendation systems.
- Cosine similarity.
- Basic trend forecasting using Linear Regression.
- Machine learning classification.
- Model evaluation and confusion matrices.
- Building interactive dashboards with Streamlit.
- Creating interactive visualizations with Plotly.
- Organizing project files and presenting data science results.

---

# Internship Details

- **Organization:** Auspify Technologies
- **Program:** Data Science Internship
- **Project:** Netflix Data Analysis, Machine Learning & Business Insights Dashboard
- **Dataset:** Netflix titles dataset
- **Completed Tasks:** Tasks 1–6

---

# Developer Information

**Developed by:** Riyajul Karim Laskar  
**Project:** Netflix Data Analysis and Machine Learning  
**Internship Organization:** Auspify Technologies

This project was developed as part of a practical Data Science Internship program.

---

# Conclusion

This project demonstrates the application of data science techniques to a Netflix dataset through six practical tasks.

The work covers data preprocessing, exploratory analysis, content-based recommendations, baseline trend forecasting, machine learning classification, and interactive business insights visualization.

The project provides hands-on experience in working with data, building analytical workflows, evaluating model results, and communicating findings through visualizations and an interactive dashboard.

---

# Disclaimer

This project is intended for educational and learning purposes as part of the Auspify Technologies Data Science Internship Program.

The recommendation system relies on similarities between available content features. Forecasts are baseline estimates and do not represent actual future Netflix releases. Classification results depend on the dataset, selected features, and evaluation methodology.

This project is an independent educational analysis and is not an official Netflix product or an official Netflix business report.

---

**#Auspify #AuspifyTechnologies #AuspifyInternship #AuspifyProjects**
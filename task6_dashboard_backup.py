# Task 6: Data Science Business Insights Dashboard
# Auspify Technologies - Data Science Internship

import os
import pandas as pd
import streamlit as st
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Netflix Data Science Dashboard",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

DATA_PATH = os.path.join("outputs", "netflix_cleaned.csv")


@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            "Dataset not found. Please run task1_data_cleaning.py first."
        )

    data = pd.read_csv(DATA_PATH)

    if "date_added" in data.columns:
        data["date_added"] = pd.to_datetime(
            data["date_added"],
            errors="coerce"
        )

    if "release_year" in data.columns:
        data["release_year"] = pd.to_numeric(
            data["release_year"],
            errors="coerce"
        )

    return data


try:
    df = load_data()
except Exception as error:
    st.error(f"Unable to load dataset: {error}")
    st.stop()

# --------------------------------------------------
# Dashboard Header
# --------------------------------------------------

st.title("🎬 Netflix Data Science Dashboard")

st.markdown(
    """
    Explore Netflix movies and TV shows through interactive charts,
    content trends, country distributions, and business insights.
    """
)

st.divider()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("🔎 Dashboard Filters")

if "type" in df.columns:
    available_types = sorted(df["type"].dropna().unique().tolist())

    selected_types = st.sidebar.multiselect(
        "Select Content Type",
        options=available_types,
        default=available_types
    )

    filtered_df = df[df["type"].isin(selected_types)].copy()
else:
    filtered_df = df.copy()

if "release_year" in filtered_df.columns:
    valid_years = filtered_df["release_year"].dropna()

    if not valid_years.empty:
        min_year = int(valid_years.min())
        max_year = int(valid_years.max())

        selected_years = st.sidebar.slider(
            "Select Release Year Range",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )

        filtered_df = filtered_df[
            filtered_df["release_year"].between(
                selected_years[0],
                selected_years[1]
            )
        ]

st.sidebar.caption("Charts update automatically when filters change.")

# --------------------------------------------------
# Key Performance Indicators
# --------------------------------------------------

total_titles = len(filtered_df)

if "type" in filtered_df.columns:
    total_movies = (filtered_df["type"] == "Movie").sum()
    total_tv_shows = (filtered_df["type"] == "TV Show").sum()
else:
    total_movies = 0
    total_tv_shows = 0

if "country" in filtered_df.columns:
    total_countries = (
        filtered_df["country"]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .replace("", pd.NA)
        .nunique()
    )
else:
    total_countries = 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", f"{total_titles:,}")
col2.metric("🎬 Movies", f"{total_movies:,}")
col3.metric("📺 TV Shows", f"{total_tv_shows:,}")
col4.metric("🌍 Countries", f"{total_countries:,}")

st.divider()

# --------------------------------------------------
# Content Type Distribution
# --------------------------------------------------

st.subheader("📊 Content Type Distribution")

if "type" in filtered_df.columns and not filtered_df.empty:
    type_counts = (
        filtered_df["type"]
        .value_counts()
        .rename_axis("Content Type")
        .reset_index(name="Count")
    )

    fig_type = px.pie(
        type_counts,
        names="Content Type",
        values="Count",
        hole=0.45,
        title="Movies vs TV Shows"
    )

    st.plotly_chart(fig_type, use_container_width=True)
else:
    st.info("No content available for the selected filters.")

# --------------------------------------------------
# Release Year Trend
# --------------------------------------------------

st.subheader("📈 Content Release Trends")

if "release_year" in filtered_df.columns:
    trend_data = (
        filtered_df.dropna(subset=["release_year"])
        .groupby("release_year")
        .size()
        .reset_index(name="Number of Titles")
        .sort_values("release_year")
    )

    if not trend_data.empty:
        fig_trend = px.line(
            trend_data,
            x="release_year",
            y="Number of Titles",
            markers=True,
            title="Number of Titles by Release Year"
        )

        fig_trend.update_layout(
            xaxis_title="Release Year",
            yaxis_title="Number of Titles"
        )

        st.plotly_chart(fig_trend, use_container_width=True)
    else:
        st.info("No release-year data available.")

# --------------------------------------------------
# Top Countries
# --------------------------------------------------

st.subheader("🌍 Top 10 Countries")

if "country" in filtered_df.columns:
    country_data = filtered_df.dropna(subset=["country"]).copy()

    country_data["country"] = country_data["country"].astype(str)

    country_data["country"] = country_data["country"].str.split(",")

    country_data = country_data.explode("country")

    country_data["country"] = country_data["country"].str.strip()

    country_data = country_data[
        country_data["country"] != ""
        ]

    top_countries = (
        country_data["country"]
        .value_counts()
        .head(10)
        .rename_axis("Country")
        .reset_index(name="Number of Titles")
    )

    if not top_countries.empty:
        fig_country = px.bar(
            top_countries.sort_values("Number of Titles"),
            x="Number of Titles",
            y="Country",
            orientation="h",
            title="Top 10 Countries by Title Count"
        )

        st.plotly_chart(fig_country, use_container_width=True)
    else:
        st.info("No country data available.")

# --------------------------------------------------
# Top Categories
# --------------------------------------------------

st.subheader("🗂️ Top 10 Categories")

if "listed_in" in filtered_df.columns:
    category_data = filtered_df.dropna(subset=["listed_in"]).copy()

    category_data["listed_in"] = (
        category_data["listed_in"].astype(str).str.split(",")
    )

    category_data = category_data.explode("listed_in")

    category_data["listed_in"] = category_data["listed_in"].str.strip()

    top_categories = (
        category_data["listed_in"]
        .value_counts()
        .head(10)
        .rename_axis("Category")
        .reset_index(name="Number of Titles")
    )

    if not top_categories.empty:
        fig_category = px.bar(
            top_categories.sort_values("Number of Titles"),
            x="Number of Titles",
            y="Category",
            orientation="h",
            title="Top 10 Netflix Categories"
        )

        st.plotly_chart(fig_category, use_container_width=True)
    else:
        st.info("No category data available.")

# --------------------------------------------------
# Ratings Distribution
# --------------------------------------------------

st.subheader("⭐ Ratings Distribution")

if "rating" in filtered_df.columns:
    rating_data = (
        filtered_df["rating"]
        .fillna("Unknown")
        .value_counts()
        .rename_axis("Rating")
        .reset_index(name="Count")
    )

    fig_rating = px.bar(
        rating_data,
        x="Rating",
        y="Count",
        title="Content Ratings Distribution"
    )

    st.plotly_chart(fig_rating, use_container_width=True)

# --------------------------------------------------
# Business Insights
# --------------------------------------------------

st.divider()
st.subheader("💡 Business Insights")

if not filtered_df.empty:

    if "type" in filtered_df.columns:
        movie_count = (filtered_df["type"] == "Movie").sum()
        tv_count = (filtered_df["type"] == "TV Show").sum()

        if movie_count > tv_count:
            st.write(
                f"- Movies are the larger content group in the current selection "
                f"({movie_count:,} Movies versus {tv_count:,} TV Shows)."
            )
        elif tv_count > movie_count:
            st.write(
                f"- TV Shows are the larger content group in the current selection "
                f"({tv_count:,} TV Shows versus {movie_count:,} Movies)."
            )
        else:
            st.write("- Movies and TV Shows have equal counts in this selection.")

    if "release_year" in filtered_df.columns:
        valid_release_years = filtered_df["release_year"].dropna()

        if not valid_release_years.empty:
            latest_year = int(valid_release_years.max())
            earliest_year = int(valid_release_years.min())

            st.write(
                f"- The selected dataset covers release years "
                f"{earliest_year} to {latest_year}."
            )

    if "listed_in" in filtered_df.columns:
        categories = (
            filtered_df["listed_in"]
            .dropna()
            .astype(str)
            .str.split(",")
            .explode()
            .str.strip()
        )

        if not categories.empty:
            popular_category = categories.value_counts().idxmax()

            st.write(
                f"- The most frequent category in the current selection "
                f"is **{popular_category}**."
            )

    st.info(
        "These observations describe the selected dataset. "
        "They do not, by themselves, establish viewer preferences, "
        "content profitability, or future demand."
    )

else:
    st.warning("No records match the selected filters.")

# --------------------------------------------------
# Data Preview and Download
# --------------------------------------------------

st.divider()
st.subheader("📋 Dataset Preview")

st.dataframe(filtered_df.head(100), use_container_width=True)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Dataset",
    data=csv_data,
    file_name="netflix_filtered_data.csv",
    mime="text/csv"
)

st.divider()

st.markdown(
    "<h4 style='text-align: center;'>"
    "Developed by Riyajul Karim Laskar"
    "</h4>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "Netflix Data Science Dashboard"
    "</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "Data Science Internship Project | Auspify Technologies"
    "</p>",
    unsafe_allow_html=True
)
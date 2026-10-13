# Task 6: Data Science Business Insights Dashboard
# Auspify Technologies - Data Science Internship
# Developer: Riyajul Karim Laskar
#
# Run with:  streamlit run netflix_dashboard.py

import os

import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Netflix Data Science Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# Design Tokens
# --------------------------------------------------

NETFLIX_RED = "#E50914"
RED_DARK = "#B20710"
BG = "#0B0B0F"
SURFACE = "#15151B"
SURFACE_ALT = "#1C1C24"
BORDER = "#2A2A35"
TEXT = "#F5F5F7"
MUTED = "#9A9AA8"

CHART_COLORS = [NETFLIX_RED, "#8C8C99", "#F5F5F7", RED_DARK, "#5A5A66"]

# --------------------------------------------------
# Global CSS
# --------------------------------------------------

st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"], .stApp {{
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }}

        .stApp {{
            background:
                radial-gradient(1200px 500px at 85% -10%, rgba(229, 9, 20, 0.14), transparent 60%),
                {BG};
            color: {TEXT};
        }}

        /* Hide default Streamlit chrome */
        #MainMenu, footer {{ visibility: hidden; }}
        header[data-testid="stHeader"] {{ background: transparent; }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1280px;
        }}

        /* Headings */
        h1, h2, h3, h4 {{
            color: {TEXT};
            letter-spacing: -0.01em;
        }}

        /* Hero header */
        .hero {{
            padding: 1.6rem 1.8rem;
            border-radius: 16px;
            background: linear-gradient(135deg, {SURFACE} 0%, {SURFACE_ALT} 100%);
            border: 1px solid {BORDER};
            border-left: 5px solid {NETFLIX_RED};
            margin-bottom: 1.5rem;
        }}
        .hero h1 {{
            margin: 0 0 0.35rem 0;
            font-size: 2rem;
            font-weight: 800;
        }}
        .hero h1 span {{ color: {NETFLIX_RED}; }}
        .hero p {{
            margin: 0;
            color: {MUTED};
            font-size: 1rem;
            line-height: 1.55;
        }}

        /* Section headings */
        .section-title {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin: 2rem 0 0.9rem 0;
            font-size: 1.25rem;
            font-weight: 700;
            color: {TEXT};
        }}
        .section-title::before {{
            content: "";
            width: 4px;
            height: 1.3rem;
            border-radius: 2px;
            background: {NETFLIX_RED};
        }}

        /* KPI cards */
        .kpi-card {{
            background: {SURFACE};
            border: 1px solid {BORDER};
            border-top: 3px solid {NETFLIX_RED};
            border-radius: 14px;
            padding: 1.1rem 1.25rem;
            transition: transform 0.15s ease, border-color 0.15s ease;
        }}
        .kpi-card:hover {{
            transform: translateY(-2px);
            border-color: {NETFLIX_RED};
        }}
        .kpi-label {{
            color: {MUTED};
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }}
        .kpi-value {{
            color: {TEXT};
            font-size: 2.1rem;
            font-weight: 800;
            line-height: 1.2;
            margin-top: 0.3rem;
        }}

        /* Insight cards */
        .insight {{
            background: {SURFACE};
            border: 1px solid {BORDER};
            border-left: 4px solid {NETFLIX_RED};
            border-radius: 10px;
            padding: 0.85rem 1.1rem;
            margin-bottom: 0.65rem;
            color: {TEXT};
            font-size: 0.97rem;
            line-height: 1.55;
        }}
        .insight b {{ color: {NETFLIX_RED}; }}

        /* Sidebar */
        /* Improved sidebar readability */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {{
    color: {TEXT} !important;
    font-weight: 600;
}}

section[data-testid="stSidebar"] .sidebar-sub {{
    color: #B8B8C5;
}}

section[data-testid="stSidebar"] .sidebar-stat {{
    color: #C5C5D0;
    line-height: 1.7;
}}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
    color: #B8B8C5;
}}

section[data-testid="stSidebar"] input {{
    accent-color: {NETFLIX_RED};
}}
            font-size: 1.6rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            color: {NETFLIX_RED};
            margin-bottom: 0.1rem;
        }}
        .sidebar-sub {{
            color: {MUTED};
            font-size: 0.8rem;
            margin-bottom: 1rem;
        }}
        .sidebar-stat {{
            background: {SURFACE};
            border: 1px solid {BORDER};
            border-radius: 10px;
            padding: 0.7rem 0.9rem;
            margin-top: 1rem;
            color: {MUTED};
            font-size: 0.82rem;
        }}
        .sidebar-stat b {{ color: {TEXT}; font-size: 1.05rem; }}

        /* Multiselect tags in red */
        span[data-baseweb="tag"] {{
            background-color: {NETFLIX_RED} !important;
            color: white !important;
            border-radius: 6px;
        }}

        /* Buttons */
        .stDownloadButton button {{
            background: {NETFLIX_RED};
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.3rem;
            font-weight: 600;
            transition: background 0.15s ease;
        }}
        .stDownloadButton button:hover {{
            background: {RED_DARK};
            color: white;
            border: none;
        }}

        /* Dividers and dataframe */
        hr {{ border-color: {BORDER} !important; }}
        div[data-testid="stDataFrame"] {{
            border: 1px solid {BORDER};
            border-radius: 12px;
            overflow: hidden;
        }}

        /* Chart containers */
        div[data-testid="stPlotlyChart"] {{
            background: {SURFACE};
            border: 1px solid {BORDER};
            border-radius: 14px;
            padding: 0.5rem;
        }}

        /* Footer */
        .footer {{
            text-align: center;
            padding: 1.5rem 0 0.5rem 0;
            color: {MUTED};
        }}
        .footer .name {{
            color: {TEXT};
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }}
        .footer .name span {{ color: {NETFLIX_RED}; }}
        .footer .small {{ font-size: 0.8rem; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Helpers
# --------------------------------------------------


def section(title: str) -> None:
    """Render a styled section heading."""
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def kpi_card(label: str, value: str) -> str:
    return (
        f'<div class="kpi-card">'
        f'<div class="kpi-label">{label}</div>'
        f'<div class="kpi-value">{value}</div>'
        f"</div>"
    )


def insight(text_html: str) -> None:
    st.markdown(f'<div class="insight">{text_html}</div>', unsafe_allow_html=True)


def style_figure(fig, height: int = 420):
    """Apply a consistent dark Netflix-style theme to a Plotly figure."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, Segoe UI, sans-serif", color=TEXT, size=14),
        title=dict(font=dict(size=17, color=TEXT), x=0.02, xanchor="left"),
        margin=dict(l=30, r=25, t=70, b=35),
        height=height,
        hoverlabel=dict(bgcolor=SURFACE_ALT, font_color=TEXT, bordercolor=NETFLIX_RED),
        legend=dict(font=dict(color=MUTED)),
    )
    fig.update_xaxes(gridcolor=BORDER, zerolinecolor=BORDER, linecolor=BORDER)
    fig.update_yaxes(gridcolor=BORDER, zerolinecolor=BORDER, linecolor=BORDER)
    return fig


def show_chart(fig) -> None:
    """Display a Plotly chart full-width (compatible with old and new Streamlit)."""
    try:
        st.plotly_chart(fig, width="stretch")
    except TypeError:
        st.plotly_chart(fig, use_container_width=True)


def show_dataframe(data: pd.DataFrame) -> None:
    try:
        st.dataframe(
            data,
            width="stretch",
            height=400,
            hide_index=True,
        )
    except TypeError:
        st.dataframe(
            data,
            use_container_width=True,
            height=400,
            hide_index=True,
        )


def explode_multivalue(series: pd.Series) -> pd.Series:
    """Split comma-separated values into one row each (same logic as original)."""
    return (
        series.dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .replace("", pd.NA)
        .dropna()
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
        data["date_added"] = pd.to_datetime(data["date_added"], errors="coerce")

    if "release_year" in data.columns:
        data["release_year"] = pd.to_numeric(data["release_year"], errors="coerce")

    return data


try:
    df = load_data()
except Exception as error:
    st.error(f"Unable to load dataset: {error}")
    st.stop()

# --------------------------------------------------
# Dashboard Header
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>🎬 Netflix <span>Data Science</span> Dashboard</h1>
        <p>Explore Netflix movies and TV shows through interactive charts,
        content trends, country distributions, and business insights.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.markdown(
    '<div class="sidebar-brand">NETFLIX</div>'
    '<div class="sidebar-sub">Data Science Dashboard</div>',
    unsafe_allow_html=True,
)

st.sidebar.header("🔎 Dashboard Filters")

if "type" in df.columns:
    available_types = sorted(df["type"].dropna().unique().tolist())

    selected_types = st.sidebar.multiselect(
        "Select Content Type",
        options=available_types,
        default=available_types,
    )

    filtered_df = df[df["type"].isin(selected_types)].copy()
else:
    filtered_df = df.copy()

if "release_year" in filtered_df.columns:
    valid_years = filtered_df["release_year"].dropna()

    if not valid_years.empty:
        min_year = int(valid_years.min())
        max_year = int(valid_years.max())

        # A slider needs min < max; with a single year there is nothing to select.
        if min_year < max_year:
            selected_years = st.sidebar.slider(
                "Select Release Year Range",
                min_value=min_year,
                max_value=max_year,
                value=(min_year, max_year),
            )

            filtered_df = filtered_df[
                filtered_df["release_year"].between(
                    selected_years[0], selected_years[1]
                )
            ]
        else:
            st.sidebar.caption(f"All titles in the selection were released in {min_year}.")

st.sidebar.markdown(
    f'<div class="sidebar-stat">Titles in current selection<br>'
    f"<b>{len(filtered_df):,}</b> of {len(df):,}</div>",
    unsafe_allow_html=True,
)
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
col1.markdown(kpi_card("Total Titles", f"{total_titles:,}"), unsafe_allow_html=True)
col2.markdown(kpi_card("🎬 Movies", f"{total_movies:,}"), unsafe_allow_html=True)
col3.markdown(kpi_card("📺 TV Shows", f"{total_tv_shows:,}"), unsafe_allow_html=True)
col4.markdown(kpi_card("🌍 Countries", f"{total_countries:,}"), unsafe_allow_html=True)

# --------------------------------------------------
# Content Type Distribution + Release Trend
# --------------------------------------------------

section("📊 Content Overview")

left, right = st.columns([1, 1.6])

with left:
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
            hole=0.55,
            title="Movies vs TV Shows",
            color_discrete_sequence=CHART_COLORS,
        )
        fig_type.update_traces(
            textinfo="percent+label",
            marker=dict(line=dict(color=BG, width=3)),
        )
        fig_type.update_layout(showlegend=False)
        show_chart(style_figure(fig_type))
    else:
        st.info("No content available for the selected filters.")

with right:
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
                title="Number of Titles by Release Year",
            )
            fig_trend.update_traces(
                line=dict(color=NETFLIX_RED, width=3),
                marker=dict(size=6, color=NETFLIX_RED),
            )
            fig_trend.update_layout(
                xaxis_title="Release Year", yaxis_title="Number of Titles"
            )
            show_chart(style_figure(fig_trend))
        else:
            st.info("No release-year data available.")

# --------------------------------------------------
# Top Countries and Categories
# --------------------------------------------------

section("🌍 Geography and Genres")

left, right = st.columns(2)

with left:
    if "country" in filtered_df.columns:
        country_values = explode_multivalue(filtered_df["country"])

        top_countries = (
            country_values.value_counts()
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
                title="Top 10 Countries by Title Count",
                color_discrete_sequence=[NETFLIX_RED],
            )
            fig_country.update_traces(marker_line_width=0)
            show_chart(style_figure(fig_country, height=460))
        else:
            st.info("No country data available.")

with right:
    if "listed_in" in filtered_df.columns:
        category_values = explode_multivalue(filtered_df["listed_in"])

        top_categories = (
            category_values.value_counts()
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
                title="Top 10 Netflix Categories",
                color_discrete_sequence=[RED_DARK],
            )
            fig_category.update_traces(marker_line_width=0)
            show_chart(style_figure(fig_category, height=460))
        else:
            st.info("No category data available.")

# --------------------------------------------------
# Ratings Distribution
# --------------------------------------------------

section("⭐ Ratings Distribution")

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
        title="Content Ratings Distribution",
        color_discrete_sequence=[NETFLIX_RED],
    )
    fig_rating.update_traces(marker_line_width=0)
    show_chart(style_figure(fig_rating, height=400))

# --------------------------------------------------
# Business Insights
# --------------------------------------------------

section("💡 Business Insights")

if not filtered_df.empty:

    if "type" in filtered_df.columns:
        movie_count = (filtered_df["type"] == "Movie").sum()
        tv_count = (filtered_df["type"] == "TV Show").sum()

        if movie_count > tv_count:
            insight(
                f"Movies are the larger content group in the current selection "
                f"(<b>{movie_count:,}</b> Movies versus <b>{tv_count:,}</b> TV Shows)."
            )
        elif tv_count > movie_count:
            insight(
                f"TV Shows are the larger content group in the current selection "
                f"(<b>{tv_count:,}</b> TV Shows versus <b>{movie_count:,}</b> Movies)."
            )
        else:
            insight("Movies and TV Shows have equal counts in this selection.")

    if "release_year" in filtered_df.columns:
        valid_release_years = filtered_df["release_year"].dropna()

        if not valid_release_years.empty:
            latest_year = int(valid_release_years.max())
            earliest_year = int(valid_release_years.min())

            insight(
                f"The selected dataset covers release years "
                f"<b>{earliest_year}</b> to <b>{latest_year}</b>."
            )

    if "listed_in" in filtered_df.columns:
        categories = explode_multivalue(filtered_df["listed_in"])

        if not categories.empty:
            popular_category = categories.value_counts().idxmax()

            insight(
                f"The most frequent category in the current selection "
                f"is <b>{popular_category}</b>."
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

section("📋 Dataset Preview")

show_dataframe(filtered_df.head(100))
st.caption(f"Showing the first {min(100, len(filtered_df)):,} of {len(filtered_df):,} filtered records.")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Dataset",
    data=csv_data,
    file_name="netflix_filtered_data.csv",
    mime="text/csv",
)

st.divider()

st.markdown(
    """
    <div class="footer">
        <div class="name">Developed by <span>Riyajul Karim Laskar</span></div>
        <div class="small">Netflix Data Science Dashboard</div>
        <div class="small">Data Science Internship Project | Auspify Technologies</div>
    </div>
    """,
    unsafe_allow_html=True,
)
# app.py
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud

# -------------------------------
# Load cleaned data
# -------------------------------
try:
    df = pd.read_csv("data/jobs_clean.csv")
except FileNotFoundError:
    st.error("Cleaned CSV not found. Please run clean_data.py first.")
    st.stop()

# Ensure essential columns exist
for col in ["Title", "Location", "Company"]:
    if col not in df.columns:
        df[col] = None

st.title("Job Market Analysis: Data Engineers")

# -------------------------------
# Sidebar filters
# -------------------------------
location_options = df["Location"].dropna().unique()
company_options = df["Company"].dropna().unique()

location_filter = st.sidebar.multiselect(
    "Filter by Location",
    options=location_options,
    default=list(location_options),
)
company_filter = st.sidebar.multiselect(
    "Filter by Company", options=company_options, default=list(company_options)
)

# Filter dataframe
filtered_df = df[
    df["Location"].isin(location_filter) & df["Company"].isin(company_filter)
]

# Handle empty filtered dataframe
if filtered_df.empty:
    st.warning("No jobs found for selected filters. Showing all data instead.")
    filtered_df = df.copy()

st.subheader("Filtered Job Data")
st.dataframe(filtered_df.head(20))

# -------------------------------
# Top Locations
# -------------------------------
top_locations = filtered_df["Location"].value_counts().head(10)
st.subheader("Top 10 Job Locations")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x=top_locations.values, y=top_locations.index, palette="viridis", ax=ax
)
ax.set_xlabel("Number of Jobs")
ax.set_ylabel("Location")
st.pyplot(fig)

# -------------------------------
# Top Companies
# -------------------------------
top_companies = filtered_df["Company"].value_counts().head(10)
st.subheader("Top 10 Companies Hiring")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x=top_companies.values, y=top_companies.index, palette="magma", ax=ax
)
ax.set_xlabel("Number of Jobs")
ax.set_ylabel("Company")
st.pyplot(fig)

# -------------------------------
# Skills WordCloud
# -------------------------------
skills_list = [
    "Python",
    "SQL",
    "Spark",
    "AWS",
    "Docker",
    "Kafka",
    "Airflow",
    "Pandas",
    "React",
    "Databricks",
    "AI",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
]
skills_count = Counter()

for title in filtered_df["Title"].dropna():
    title_lower = str(title).lower()
    for skill in skills_list:
        if skill.lower() in title_lower:
            skills_count[skill] += 1

st.subheader("Most In-Demand Skills")
if skills_count:
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(skills_count)
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("No skills found in the current filtered data.")

# -------------------------------
# Salary Distribution (if available)
# -------------------------------
if (
    "Salary_Clean" in filtered_df.columns
    and filtered_df["Salary_Clean"].notna().any()
):
    st.subheader("Salary Distribution")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(
        filtered_df["Salary_Clean"].dropna(),
        bins=20,
        kde=True,
        color="skyblue",
        ax=ax,
    )
    ax.set_xlabel("Salary ($)")
    ax.set_ylabel("Number of Jobs")
    st.pyplot(fig)
else:
    st.info("Salary data not available for this dataset.")

# scripts/clean_data.py
import re
from collections import Counter

import pandas as pd


def parse_salary(s):
    """Extract numeric salary from a string."""
    if pd.isna(s):
        return None

    s_clean = re.sub(r"[\$,]", "", str(s))
    match = re.search(r"\d+", s_clean)

    return int(match.group()) if match else None


def clean_jobs_data():
    """Clean scraped job data."""
    try:
        df = pd.read_csv("data/jobs_raw.csv")
    except FileNotFoundError:
        print("Error: data/jobs_raw.csv not found.")
        return None

    df.drop_duplicates(inplace=True)

    if "Location" in df.columns:
        df["Location"] = (
            df["Location"]
            .astype(str)
            .str.replace(r"\s*\(.*\)", "", regex=True)
            .str.strip()
        )

    if "Salary" in df.columns:
        df["Salary_Clean"] = df["Salary"].apply(parse_salary)
    else:
        df["Salary_Clean"] = None

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

    if "Title" in df.columns:
        for title in df["Title"].dropna():
            title_lower = str(title).lower()

            for skill in skills_list:
                if skill.lower() in title_lower:
                    skills_count[skill] += 1

    df.to_csv("data/jobs_clean.csv", index=False)

    print("Data cleaning complete!")
    print("Top skills:", dict(skills_count))

    return df


if __name__ == "__main__":
    clean_jobs_data()

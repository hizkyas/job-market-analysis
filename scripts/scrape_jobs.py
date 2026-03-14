import os

import pandas as pd
import requests

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Search parameters
keywords = ["data engineer", "ai engineer"]

jobs = []

for keyword in keywords:
    print(f"Fetching jobs for: {keyword}")

    url = "https://remotive.com/api/remote-jobs"
    params = {"search": keyword}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Failed to fetch data")
        continue

    data = response.json()

    for job in data["jobs"]:
        jobs.append(
            {
                "Title": job.get("title"),
                "Company": job.get("company_name"),
                "Location": job.get("candidate_required_location"),
                "Category": job.get("category"),
                "Job Type": job.get("job_type"),
                "Publication Date": job.get("publication_date"),
                "URL": job.get("url"),
            }
        )

# Convert to DataFrame
df = pd.DataFrame(jobs)

# Remove duplicates
df = df.drop_duplicates()

# Save to CSV
file_path = "data/jobs_raw.csv"
df.to_csv(file_path, index=False)

print(f"Scraping complete. {len(df)} jobs saved to {file_path}")

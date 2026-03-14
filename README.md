# 📊 Job Market Analysis Data Pipeline

A production-style **Data Engineering project** that collects, processes, and visualizes job market data for **Data Engineers and AI Engineers**.  
The project demonstrates an end-to-end **data pipeline with automated testing, linting, and CI/CD**.

It scrapes job postings, cleans the dataset, extracts demanded skills, and presents insights through an interactive **Streamlit dashboard**.

---

# 🚀 Project Overview

The **Job Market Analysis pipeline** automates the process of collecting and analyzing job market trends.  
It follows a modular architecture separating **data ingestion, processing, analysis, and visualization**.

## Key Features

**Automated Data Pipeline**
- Scrapes job postings from online job boards
- Stores raw datasets for reproducibility

**Data Cleaning & Processing**
- Removes duplicates
- Standardizes location data
- Parses salary information
- Extracts skills from job titles

**Data Insights**
- Top hiring locations
- Companies actively hiring
- Most demanded technical skills

**Interactive Dashboard**
- Built with **Streamlit**
- Filter jobs by company and location
- Visualize hiring trends

**Production Practices**
- Code linting with **flake8**
- Code formatting with **black**
- Automated testing with **pytest**
- CI/CD pipeline via **GitHub Actions**

---

# 🛠️ Tech Stack

**Language**

Python 3.11+

**Data Processing**

Pandas  
NumPy  

**Visualization**

Matplotlib  
Seaborn  
WordCloud  

**Frontend / Dashboard**

Streamlit  

**Data Engineering Tools**

Pytest  
Flake8  
Black  

**DevOps**

Git  
GitHub Actions (CI/CD)

---

# 📁 Project Structure

```
job-market-analysis/
│
├── app.py                   # Streamlit dashboard
├── run_pipeline.py          # Local CI pre-flight script
├── requirements.txt
├── README.md
│
├── data/
│   ├── jobs_raw.csv         # Raw scraped data
│   └── jobs_clean.csv       # Cleaned dataset
│
├── scripts/
│   ├── __init__.py
│   ├── scrape_jobs.py       # Job scraping script
│   └── clean_data.py        # Data cleaning pipeline
│
├── tests/
│   └── test_clean.py        # Unit tests
│
└── .github/
    └── workflows/
        └── ci_cd.yml        # CI/CD pipeline
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```
git clone https://github.com/hizkyas/job-market-analysis.git
cd job-market-analysis
```

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment (Windows)

```
venv\Scripts\activate
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔄 Run the Data Pipeline

### Run Web Scraper

```
python scripts/scrape_jobs.py
```

### Clean the Dataset

```
python scripts/clean_data.py
```

---

# 📊 Launch the Dashboard

```
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

The dashboard provides:

- Job distribution by location
- Top hiring companies
- Most demanded skills (WordCloud)
- Interactive filtering

---

# 🧪 Testing

Run unit tests:

```
pytest
```

Lint code:

```
flake8
```

Format code:

```
black .
```

---

# 🧪 Local CI Pipeline

Before pushing to GitHub, run the full pipeline locally:

```
python run_pipeline.py
```

This verifies:

- Linting
- Unit tests
- Scraper execution
- Data cleaning
- Dashboard validation

---

# ⚡ CI/CD Pipeline

GitHub Actions automatically runs on each push:

- Code linting
- Unit testing
- Pipeline validation

This ensures the project remains **production-ready**.

---

# 📈 Example Insights

The analysis provides insights such as:

- Which cities hire the most **Data Engineers**
- Companies actively recruiting AI/ML talent
- Most demanded technologies (Python, SQL, AWS, etc.)

---

# 🔮 Future Improvements

- Scheduled scraping using **Airflow**
- Deploy dashboard to **cloud infrastructure**
- Add **NLP skill extraction**
- Add **salary prediction model**

---

# 👤 Author

**Hizkyas Tadele**

AI / Data Engineer  
Cybersecurity Analyst at Commercial Bank of Ethiopia  

GitHub  
https://github.com/hizkyas

---

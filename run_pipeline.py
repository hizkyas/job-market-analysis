import subprocess
import sys


def run_step(name, command):
    print(f"\n===== Running: {name} =====")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(f"\n❌ {name} FAILED")
        sys.exit(1)

    print(f"✅ {name} PASSED")


def main():
    run_step(
        "Flake8 Lint",
        "flake8 . --exclude venv,__pycache__",
    )

    run_step(
        "Unit Tests",
        "pytest",
    )

    run_step(
        "Scraper",
        "python scripts/scrape_jobs.py",
    )

    run_step(
        "Data Cleaning",
        "python scripts/clean_data.py",
    )

    run_step(
        "Streamlit Syntax Check",
        "python -m py_compile app.py",
    )

    print("\n🎉 ALL CHECKS PASSED — SAFE TO PUSH TO GITHUB")


if __name__ == "__main__":
    main()

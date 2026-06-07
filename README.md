# ETL Project — Countries GDP (Nominal)

Description
- A small ETL script that extracts country GDP (nominal) data from a saved Wikipedia snapshot, parses the table, and produces a pandas DataFrame. The script currently fetches the archived page, extracts the table of countries and their GDP (USD, millions) and prints the resulting DataFrame. Several ETL helper functions are scaffolded for transform, CSV export, and database load.

What the script does
- Extract: scrapes the archived Wikipedia page and builds a DataFrame with `Country` and `GDP(USD_Millions)` columns.
- Transform: (scaffolded) intended to convert currency strings to numeric values and rescale from millions to billions.
- Load: (scaffolded) intended to export to CSV and load into a SQLite database.

Files
- `etl_pj_gdp.py` — main ETL script (extract function implemented; other functions scaffolded).

Requirements
- Python 3.8+
- Python packages:
	- requests
	- beautifulsoup4
	- pandas
	- numpy

Install packages:

```bash
# install packages individually
pip install requests beautifulsoup4 pandas numpy
```

Quick start
1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python etl_pj_gdp.py
```

Notes and next steps
- The `transform`, `load_to_csv`, and `load_to_db` functions are currently placeholders. Implement them to export results to `Countries_GDP.csv` and persist into a SQLite database (`economy.db`) if needed.
- The extraction relies on a specific snapshot and a particular table index; changes to the source HTML structure may break the scraper.

Uploading to GitHub
- Initialize a git repo, commit files, then push to a new GitHub repository. Example commands:

```bash
git init
git add .
git commit -m "Add ETL GDP script and README"
# create a repository on GitHub (via website) and then:
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

If you want, I can implement the missing transform/load functions or create the repository and push these files for you — tell me which you prefer.

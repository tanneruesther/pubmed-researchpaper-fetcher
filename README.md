PubMed Research Paper Fetcher
A Python command-line tool to fetch research papers from PubMed based on a user-specified query. It extracts papers with at least one non-academic author (e.g., authors affiliated with pharmaceutical or biotech companies) and returns the results in a structured CSV format.

Features
Fetches papers using PubMed's Entrez API via BioPython.

Supports full PubMed query syntax.

Filters authors based on non-academic company affiliations using keyword heuristics.

Extracts corresponding author emails from affiliation text.

Outputs a structured CSV file with relevant paper metadata.

Fully functional command-line interface using argparse.

Uses typed Python with mypy support for safe and maintainable code.

Published on TestPyPI for testing and distribution.

Project Structure
graphql
Copy
Edit
pubmed-researchpaper-fetcher/
├── cli.py                 # Entry point for the CLI
├── pyproject.toml         # Poetry configuration
├── README.md              # Project documentation
├── get_papers/
│   ├── __init__.py
│   ├── pubmed.py          # Logic to fetch papers from PubMed
│   ├── filter.py          # Filtering and email extraction
│   ├── writer.py          # CSV writing with pandas
│   └── utils.py           # Safe Entrez API call handler
├── test_fetch.py          # Script to test filtering logic
└── output.csv             # Optional sample CSV output
Installation
Step 1: Clone the repository
bash
Copy
Edit
git clone https://github.com/tanneruesther/pubmed-researchpaper-fetcher.git
cd pubmed-researchpaper-fetcher
Step 2: Install dependencies using Poetry
bash
Copy
Edit
poetry install
Step 3: Activate the virtual environment
bash
Copy
Edit
poetry shell
Usage
bash
Copy
Edit
get-papers-list -q "Pfizer COVID-19" -m 50 -f output.csv --only-non-academic --debug
Command-line Options
Flag	Description
-q, --query	(Required) PubMed search query
-m, --max	Max number of results to fetch (default: 100)
-f, --file	Output CSV filename (prints to console if not provided)
-o, --only-non-academic	Filter only papers with non-academic/company affiliations
-d, --debug	Print debug information during execution
-h, --help	Show help message and usage instructions

Output Format
If --only-non-academic is used, the CSV will contain:

Column	Description
PubmedID	Unique identifier of the paper
Title	Title of the research article
Publication Date	Year the paper was published
Non-academic Author(s)	Names of authors affiliated with companies
Company Affiliation(s)	Company affiliations parsed from author metadata
Corresponding Author Email	Extracted email address from affiliations

Testing
Run a test to validate filtering logic:
bash
Copy
Edit
poetry run python test_fetch.py
Run static type checks:
bash
Copy
Edit
poetry run mypy get_papers/ cli.py
How It Works
Papers are fetched using Bio.Entrez (via esearch and efetch).

Affiliation strings are scanned for known pharmaceutical/biotech company keywords such as "Pfizer", "Moderna", "GSK", etc.

Author emails are extracted using regular expressions.

Academic affiliations are filtered using keywords like "university", "institute", "college", "hospital", etc.

Tools Used
BioPython (Entrez) - For accessing PubMed data

pandas - For exporting structured CSVs

Poetry - For dependency and environment management

mypy - For type checking and safety

Publishing
The module is published on TestPyPI for testing purposes:

https://test.pypi.org/project/pubmed-researchpaper-fetcher/

To install directly from TestPyPI:

bash
Copy
Edit
pip install --index-url https://test.pypi.org/simple/ pubmed-researchpaper-fetcher
Future Improvements
Dynamically read company names from an external configuration file.

Add comprehensive unit tests using pytest.

Enhance metadata filtering using MeSH tags.

Publish to the official PyPI registry.

License
MIT License © 2025 Tanneruesther
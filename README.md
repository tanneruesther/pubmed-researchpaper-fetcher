
# 🧬 PubMed Research Paper Fetcher

A Python command-line tool to fetch research papers from PubMed based on a user-specified query and return only those papers with **at least one non-academic author** (e.g., authors affiliated with pharmaceutical or biotech companies). It outputs cleanly formatted results as a CSV file.

---

## ✅ Features

- 🔍 Fetches papers using PubMed's Entrez API (via BioPython).
- 🧪 Supports full PubMed query syntax for flexible search.
- 🏢 Filters authors based on **non-academic company affiliations** using keyword heuristics.
- 📧 Extracts **corresponding author emails** from affiliations.
- 📄 Outputs a clean CSV file with the required fields.
- ⚙️ Fully functional **command-line interface** with flags.
- 🛡️ Typed with `mypy` support for **safe, maintainable code**.
- 📦 Published on [TestPyPI](https://test.pypi.org/project/pubmed-researchpaper-fetcher/0.1.2/).

---

## 📁 Project Structure

pubmed-researchpaper-fetcher/
├── cli.py # Entry point: CLI handler using argparse
├── pyproject.toml # Poetry configuration
├── README.md # You're reading it!
├── get_papers/
│ ├── init.py
│ ├── pubmed.py # Entrez-based paper fetching logic
│ ├── filter.py # Filtering by non-academic/company affiliations
│ ├── writer.py # CSV writing using pandas
│ └── utils.py # Safe Entrez API call wrappers
├── test_fetch.py # Test script to verify filtering logic
└── output.csv # (Optional) Output file


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/tanneruesther/pubmed-researchpaper-fetcher.git
cd pubmed-researchpaper-fetcher
**### 2. Install dependencies using Poetry**
      poetry install
3. Activate the environment
      poetry shell
🚀 Usage
        get-papers-list -q "Pfizer COVID-19" -m 50 -f output.csv --only-non-academic --debug


Command-line Options
| Flag                        | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| `-q`, `--query`             | **(Required)** PubMed search query                       |
| `-m`, `--max`               | Max number of papers to fetch (default: 100)             |
| `-f`, `--file`              | Output CSV filename (prints to console if not specified) |
| `-o`, `--only-non-academic` | Filter only papers with non-academic/company authors     |
| `-d`, `--debug`             | Print debug information                                  |
| `-h`, `--help`              | Show usage instructions                                  |


📤 Output Format
When using --only-non-academic, the CSV will include:
| Column                       | Description                         |
| ---------------------------- | ----------------------------------- |
| `PubmedID`                   | Unique ID for the paper             |
| `Title`                      | Title of the research paper         |
| `Publication Date`           | Year of publication                 |
| `Non-academic Author(s)`     | Names of company-affiliated authors |
| `Company Affiliation(s)`     | Company names found in affiliations |
| `Corresponding Author Email` | Email extracted from affiliation    |


🧪 Testing
To test if filtering logic works correctly:
      -->poetry run python test_fetch.py
    To run static type checks:
      --> poetry run mypy get_papers/ cli.py
🧱 How It Works
      Papers are fetched using Bio.Entrez (via efetch/esearch).
      Affiliations are scanned for keywords like "Pfizer", "Moderna", "GSK", etc.
      Emails are extracted using regular expressions.
      Academic affiliations are filtered using terms like "university", "institute", "college", etc.

🛠 Tools Used
        BioPython Entrez – PubMed API access
        pandas – For exporting CSVs
        Poetry – Dependency and environment management
        mypy – Type checking

📤 Publishing
      Module is published on Test PyPI:
        📦 https://test.pypi.org/project/pubmed-researchpaper-fetcher/

You can install from TestPyPI using:
     pip install -i https://test.pypi.org/simple/ pubmed-researchpaper-fetcher==0.1.2
📌 Future Improvements
 --Dynamically expand known company names via an external config file.
 --Add proper unit tests using pytest.
 --Enhance filtering using MeSH metadata (if available).
  --Publish to official PyPI.

📜 License
MIT License © 2025 Tanneruesther
Made with ❤️ for PubMed & Python




# test_fetch.py
from get_papers.pubmed import fetch_pubmed_papers

papers = fetch_pubmed_papers("Moderna COVID-19", max_results=5)
assert isinstance(papers, list)
assert all("Company Affiliation(s)" in p for p in papers)
print("✅ Test passed: Filtered papers contain company affiliations.")

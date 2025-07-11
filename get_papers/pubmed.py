
from typing import List, Dict, Any
from Bio import Entrez
from get_papers.filter import filter_non_academic, extract_email
from get_papers.utils import safe_entrez_call

# Entrez.email = "tanneruesther@gmail.com"
Entrez.email = "tanneruesther@gmail.com"  # type: ignore


def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    try:
        search_handle = safe_entrez_call(Entrez.esearch, db="pubmed", term=query, retmax=max_results)
        if not search_handle:
            return []

        search_results = Entrez.read(search_handle)
        ids = search_results.get("IdList", [])
        if not ids:
            print("⚠️ No results found.")
            return []

        fetch_handle = safe_entrez_call(Entrez.efetch, db="pubmed", id=",".join(ids), rettype="medline", retmode="xml")
        if not fetch_handle:
            return []

        records = Entrez.read(fetch_handle)
        fetch_handle.close()

        papers: List[Dict[str, Any]] = []
        for article in records["PubmedArticle"]:
            citation = article["MedlineCitation"]["Article"]
            # pmid = article["MedlineCitation"]["PMID"]
            pmid: str = str(article["MedlineCitation"].get("PMID", ""))

            title = citation.get("ArticleTitle", "No Title")
            pub_date = citation.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "Unknown")

            authors: List[str] = []
            affiliations: set[str] = set()

            for author in citation.get("AuthorList", []):
                name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                if name:
                    authors.append(name)
                for aff in author.get("AffiliationInfo", []):
                    affiliations.add(aff.get("Affiliation", ""))

            papers.append({
                "PubmedID": str(pmid),
                "Title": title,
                "Publication Date": pub_date,
                "Authors": ", ".join(authors),
                "Affiliations": "; ".join(affiliations)
            })

        return papers

    except Exception as e:
        print("❌ Error fetching data from PubMed:", e)
        return []

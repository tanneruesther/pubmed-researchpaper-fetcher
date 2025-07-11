
import re
from typing import List, Dict, Any

academic_keywords: List[str] = [
    "university", "institute", "college", "school", "faculty",
    "department", "research center", "centre", "hospital",
    "academy", "laboratory", "lab"
]

company_keywords: List[str] = [
    "pfizer", "moderna", "gsk", "roche", "novartis", "astrazeneca",
    "lilly", "biontech", "sanofi", "johnson", "abbvie", "regeneron",
    "inspirevax", "bayer", "boehringer", "takeda"
]

def is_academic(affiliation: str) -> bool:
    return any(keyword in affiliation.lower() for keyword in academic_keywords)

def is_company(affiliation: str) -> bool:
    return any(keyword in affiliation.lower() for keyword in company_keywords)

def extract_email(text: str) -> str:
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else "N/A"

def filter_non_academic(papers: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    filtered: List[Dict[str, str]] = []

    for paper in papers:
        affiliations_raw = paper.get("Affiliations", "")
        authors = paper.get("Authors", "")
        affiliations = [a.strip() for a in affiliations_raw.split(";")]

        company_affils: set[str] = set()
        email: str = "N/A"

        for aff in affiliations:
            if is_company(aff) and not is_academic(aff):
                company_affils.add(aff.strip())

            if email == "N/A":
                maybe_email = extract_email(aff)
                if maybe_email != "N/A":
                    email = maybe_email

        if company_affils:
            filtered.append({
                "PubmedID": paper.get("PubmedID", ""),
                "Title": paper.get("Title", ""),
                "Publication Date": paper.get("Publication Date", ""),
                "Non-academic Author(s)": authors,
                "Company Affiliation(s)": "; ".join(company_affils),
                "Corresponding Author Email": email
            })

    return filtered

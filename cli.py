
import argparse
from get_papers.pubmed import fetch_pubmed_papers
from get_papers.filter import filter_non_academic
from get_papers.writer import export_to_csv_with_pandas
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Search and export PubMed papers.")
    parser.add_argument('-q', '--query', required=True, help='Search query (e.g., Pfizer COVID-19)')
    parser.add_argument('-m', '--max', type=int, default=100, help='Number of results to fetch')
    parser.add_argument('-f', '--file', help='CSV output filename (if not provided, prints to console)')
    parser.add_argument('-o', '--only-non-academic', action='store_true', help='Show only papers with non-academic authors')
    parser.add_argument('-d', '--debug', action='store_true', help='Print debug information during execution')

    args = parser.parse_args()

    print(f"🔍 Searching PubMed for: {args.query}")
    papers = fetch_pubmed_papers(args.query, max_results=args.max)

    if args.debug:
        print(f"🪵 [DEBUG] Total papers fetched: {len(papers)}")

    if args.only_non_academic:
        papers = filter_non_academic(papers)
        if args.debug:
            print(f"🪵 [DEBUG] Papers after filtering non-academic: {len(papers)}")

    if not papers:
        print("⚠️ No matching papers found.")
        return

    columns = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email"
    ] if args.only_non_academic else None

    if args.file:
        export_to_csv_with_pandas(papers, filename=args.file, columns=columns)
    else:
        df = pd.DataFrame(papers)
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()


# if __name__ == "__main__":
#     main()

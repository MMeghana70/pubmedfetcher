import requests
import pandas as pd
import argparse

# Base URL for PubMed API
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query):
    """Fetch papers from PubMed based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Adjust the number of papers to fetch
    }
    
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    return paper_ids

def fetch_paper_details(paper_ids):
    """Fetch detailed information for given PubMed IDs."""
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    papers = []
    for pid in paper_ids:
        paper = data.get("result", {}).get(pid, {})
        papers.append({
            "PubmedID": pid,
            "Title": paper.get("title", "N/A"),
            "Publication Date": paper.get("pubdate", "N/A"),
            "Authors": ", ".join([a.get("name", "N/A") for a in paper.get("authors", [])]),
            "Company Affiliation": paper.get("source", "N/A"),
            "Corresponding Author Email": "N/A"
        })
    
    return papers

def save_to_csv(papers, filename):
    """Save results to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and save as CSV.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-f", "--file", help="File to save results (default: print to console).")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    paper_ids = fetch_pubmed_papers(args.query)
    papers = fetch_paper_details(paper_ids)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        print(pd.DataFrame(papers))

if __name__ == "_main_":
    main()
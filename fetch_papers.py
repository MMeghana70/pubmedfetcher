import requests
import csv

def fetch_pubmed_papers(query):
    print(f"Fetching papers for: {query}")  # Debugging

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmode=json"
    print(f"PubMed API URL: {url}")  # Debugging

    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error: Failed to fetch data from PubMed")
        return

    data = response.json()
    print("Response JSON:", data)  # Debugging

    if "esearchresult" in data and "idlist" in data["esearchresult"]:
        paper_ids = data["esearchresult"]["idlist"]
        print(f"Found {len(paper_ids)} papers.")  # Debugging
    else:
        print("No papers found.")
        return

<<<<<<< HEAD
    # Fetch details for these papers
    details_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(paper_ids)}&retmode=json"
    print(f"Fetching details from: {details_url}")  # Debugging

    details_response = requests.get(details_url)
    details_data = details_response.json()
    print("Details JSON:", details_data)  # Debugging

    # Save to CSV
    with open("papers.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Title", "Authors", "Journal", "Year", "DOI"])
        
        for paper_id in paper_ids:
            paper_info = details_data["result"].get(paper_id, {})
            title = paper_info.get("title", "No title available")
            authors = "; ".join([author["name"] for author in paper_info.get("authors", [])])
            journal = paper_info.get("source", "Unknown Journal")
            year = paper_info.get("pubdate", "Unknown Year")
            doi = paper_info.get("elocationid", "No DOI available")
            
            csv_writer.writerow([title, authors, journal, year, doi])
    
    print("✅ Papers saved to `papers.csv`")

# Run the script
if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "COVID-19"
    fetch_pubmed_papers(query)
=======
if __name__ == "_main_":
    main()
>>>>>>> 6cecb6cc1681e3a10292a420c9d46f40ce412950

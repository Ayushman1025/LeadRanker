# scraping/scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import quote

def google_search_scrape(query, num_pages=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    all_results = []

    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={quote(query)}&start={start}"
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for result in soup.select('.tF2Cxc'):
            title = result.select_one('h3')
            link = result.select_one('a')['href']
            snippet = result.select_one('.VwiC3b')
            
            if title and 'linkedin.com/in/' in link:
                all_results.append({
                    "name_title": title.get_text(),
                    "profile_url": link,
                    "snippet": snippet.get_text() if snippet else "",
                    "source": "Google"
                })

        time.sleep(1.5)  # Be nice to Google

    return pd.DataFrame(all_results)

# Example usage (can remove in final production script)
if __name__ == "__main__":
    df = google_search_scrape("CEO SaaS India site:linkedin.com/in", num_pages=2)
    print(df.head())
    df.to_csv("data/raw_leads.csv", index=False)

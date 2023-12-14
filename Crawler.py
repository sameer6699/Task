#importing necessary libraries 
import requests 
import time
import lxml
import pandas as pd 
from bs4 import BeautifulSoup

# Global variables
MAX_DEPTH = 3
VISITED = set()

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: {e}")
        return None

def parse_page(html):
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        # Extract and process data here
        # For example, find links and other information on the page.
        links = [a.get('href') for a in soup.find_all('a', href=True)]  # Use a.get('href') to avoid KeyError
        return links
    else:
        return []

def crawl_website(url, depth):
    if depth > MAX_DEPTH:
        return

    if url in VISITED:
        return

    print(f"Crawling {url} at depth {depth}...")
    html = fetch_page(url)

    if html is not None:
        links = parse_page(html)

        for link in links:
            # Ensure that the link is an absolute URL.
            if not link.startswith('http'):
                link = url + link

            crawl_website(link, depth + 1)

    VISITED.add(url)
    time.sleep(1)  # Be polite and add a delay

if __name__ == "__main__":
    starting_url = "https://nlp.stanford.edu/IR-book/information-retrieval-book.html"
    crawl_website(starting_url, depth=0)

    #Save the visited Url in CSV File 
    df = pd.DataFrame(VISITED)
    df.to_csv('visited.csv', index=False)
    print("Visited Urls are saved in visited.csv file")
    

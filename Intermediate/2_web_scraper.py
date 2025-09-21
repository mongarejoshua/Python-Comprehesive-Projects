import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    links = scrape_website(url)
    print("Found links:")
    for link in links:
        print(link)
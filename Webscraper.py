import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information based on the HTML structure of the page
        # Here, we'll just print the text content of all <p> tags
        for paragraph in soup.find_all('p'):
            print(paragraph.get_text())
    else:
        print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")

# Example usage
url_to_scrape = 'https://example.com'
simple_web_scraper(url_to_scrape)
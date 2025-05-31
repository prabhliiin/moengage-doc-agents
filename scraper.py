import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def extract_text_from_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Remove script and style tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    
    # Join only visible text
    visible_text = " ".join(chunk.strip() for chunk in soup.stripped_strings)
    
    return visible_text
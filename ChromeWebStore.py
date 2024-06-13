import requests
from bs4 import BeautifulSoup

import json

BASE_URL = "https://chromewebstore.google.com/search/"

def fetch_search_results(query):
    url = f"{BASE_URL}{query}?itemTypes=EXTENSION"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch search results. Status code: {response.status_code}")

def parse_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    items = soup.select('div.Cb7Kte')

    results = []
    for item in items:
        link_tag = item.find('a')
        title_tag = item.find('h2', class_='CiI2if')
        description_tag = item.find('p', class_='g3IrHd')
        image_url = item.find('img', class_='fzxcm')

        if link_tag and title_tag and description_tag and image_url:
            href = link_tag['href'].split("/")
            image = image_url['src']
            if len(href) == 4:
                href = href[3]
            else:
                href = href[2]
            title = title_tag.get_text(strip=True)
            description=description_tag.get_text(strip=True)
            results.append({'title': title, 'url': href, 'description': description, 'image': image})

    return json.dumps(results, indent=2)

def search(query):
    html_content = fetch_search_results(query)
    return parse_results(html_content)

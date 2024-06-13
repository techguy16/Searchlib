import requests
import json

import UserAgent

from bs4 import BeautifulSoup

headers = {
    'User-Agent': UserAgent.randomUserAgent()}

def suggestions(phrase):
    urlContent = requests.get(f"https://duckduckgo.com/ac/?q={phrase}&kl=wt-wt", headers=headers).text
    urlContent = json.loads(urlContent)
    
    suggestions = []
    for item in urlContent:
        suggestions.append(item["phrase"])
        
    return suggestions

def search(phrase):
    urlContent = requests.get(f"https://lite.duckduckgo.com/lite/?q={phrase}", headers=headers).text
    soup = BeautifulSoup(urlContent, 'html.parser')
    
    urls = []
    for links in soup.find_all("span", class_='link-text'):
        urls.append(links.string)
        
    return urls
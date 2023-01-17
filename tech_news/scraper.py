import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, wait: int = 3):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=wait)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    urls = []
    for url in selector.css(".entry-title a::attr(href)").getall():
        if url not in urls:
            urls.append(url)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)
    for next_page in selector.css(".next.page-numbers::attr(href)").getall():
        if not next_page:
            return None
        return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    data_dict = {}

    data_dict["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    data_dict["title"] = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    data_dict["timestamp"] = timestamp.strip() if timestamp else ""
    data_dict["writer"] = selector.css("span.author a::text").get()
    comments_count = selector.css(".title-block::text").re_first(r"\d+")
    data_dict["comments_count"] = int(comments_count) if comments_count else 0
    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()
    data_dict["summary"] = "".join(summary)
    data_dict["summary"] = (
        data_dict["summary"].strip() if data_dict["summary"] else "")
    data_dict["tags"] = selector.css("section.post-tags a::text").getall()
    category = selector.css(".label::text").get()
    data_dict["category"] = category.strip() if category else ""
    return data_dict


# Requisito 5
def get_tech_news(amount):
    list_news = []
    news_data = []
    get_html = fetch("https://blog.betrybe.com/")
    while len(list_news) < amount:
        list_news.extend(scrape_updates(get_html))
        next_page = scrape_next_page_link(get_html)
        get_html = fetch(next_page)
    for news in list_news[:amount]:
        get_html = fetch(news)
        news_data.append(scrape_news(get_html))
    create_news(news_data)
    return news_data

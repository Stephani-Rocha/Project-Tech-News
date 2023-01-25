from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search_title = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news_found = list()
    for news in search_title:
        new_tuple = (news["title"], news["url"])
        list_news_found.append(new_tuple)
    return list_news_found


# Requisito 7
def search_by_date(date):
    try:
        formatted_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        search_date = search_news({"timestamp": {"$eq": formatted_date}})
        list_news_found = list()
        for news in search_date:
            new_tuple = (news["title"], news["url"])
            list_news_found.append(new_tuple)
        return list_news_found
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search_tag = search_news({"tags": {"$regex": tag, "$options": "i"}})
    list_news_found = list()
    for news in search_tag:
        new_tuple = (news["title"], news["url"])
        list_news_found.append(new_tuple)
    return list_news_found


# Requisito 9
def search_by_category(category):
    search_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    list_news_found = list()
    for news in search_category:
        new_tuple = (news["title"], news["url"])
        list_news_found.append(new_tuple)
    return list_news_found

from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


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
    """Seu código deve vir aqui"""

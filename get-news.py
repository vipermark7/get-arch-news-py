from bs4 import BeautifulSoup
import requests
from xml.sax.saxutils import unescape
import re

ARCH_NEWS_URL = "https://archlinux.org/feeds/news/"


def get_news():
    news = requests.get(ARCH_NEWS_URL)
    return news


def parse_news_xml():
    return BeautifulSoup(get_news().text, 'xml')


def remove_html_tags(string):
    return re.sub("<[^<]+?>", "", string)


def print_news():
    soup = parse_news_xml()
    for item in soup.find_all("item")[0:3]:
        print()
        print(remove_html_tags(item.pubDate.text))
        print(remove_html_tags(item.title.text))
        print(remove_html_tags(unescape(item.description.text)))


parse_news_xml()
print_news()


from bs4 import BeautifulSoup
import requests
from xml.sax.saxutils import unescape

arch_news_url = "https://archlinux.org/feeds/news/"
news = requests.get(arch_news_url)
soup = BeautifulSoup(news.text, 'xml')
for description in soup.find_all("description"):
    print(unescape(description.text))









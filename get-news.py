from bs4 import BeautifulSoup
import requests
from xml.sax.saxutils import unescape

arch_news_url = "https://archlinux.org/feeds/news/"
news = requests.get(arch_news_url)
soup = BeautifulSoup(news.text, 'xml')
for item in soup.find_all("item")[0:3]:
    print()
    print(item.pubDate)
    print(item.title.text)
    print(unescape(item.description.text))









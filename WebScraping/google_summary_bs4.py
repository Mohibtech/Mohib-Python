from bs4 import BeautifulSoup
import requests
import time
from random import randint


def scrape_news_summaries(s):
    time.sleep(randint(0, 2))  # relax and don't let google be angry
    r = requests.get("http://www.google.com/search?q="+s+"&tbm=nws")
    print(r.status_code)  # Print the status codeup
    content = r.text
    news_summaries = []
    soup = BeautifulSoup(content, "html.parser")
    st_divs = soup.findAll("div", {"class": "st"})
    for st_div in st_divs:
        news_summaries.append(st_div.text)
    return news_summaries

#search = input("Enter search term")
l = scrape_news_summaries('Omni Group')
for n in l:
    print(n)
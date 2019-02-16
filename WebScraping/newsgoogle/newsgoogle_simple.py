import bs4
import lxml #xml parser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def news(xml_news_url):
	
	Client=urlopen(xml_news_url)
	xml_page=Client.read()
	Client.close()
	
	soup_page=soup(xml_page,"xml")
	
	news_list=soup_page.findAll("item")
	
	for news in news_list:
		
		print(news.title.text)
		print(news.link.text)
		print(news.pubDate.text)	
		print("\n\n")
		



#you can add google news 'xml' URL here for any country/category
term = 'Health Card Pakistan'
term = term.replace(' ','%20')
news_url = f'http://news.google.com/news?q={term}&output=rss'
 
news(news_url)	
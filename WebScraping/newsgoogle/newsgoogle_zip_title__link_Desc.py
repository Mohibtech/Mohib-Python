import requests
import bs4

titleList = []
descList = []
hrefList = []
desctitle = []
term = 'Omni Group'
keywords = [term]

for search_term in keywords:
	
	req = requests.get('https://news.google.com/news?q=%s&output=rss'%(search_term))
	soup = bs4.BeautifulSoup(req.text,'html.parser')
	title = soup.select('title')
	descript = soup.select('description')
	print ("############",search_term,"############ \n")

	for i in range(5): 
		temp = bs4.BeautifulSoup(descript[i+1].get_text(), 'html.parser')
		href = temp.select('a')
		font_text = temp.select('font')[0].get_text()
		link_desc = temp.select('p')[0].get_text()

		hrefList.append(href[0]['href'])
		titleList.append(title[i+1].get_text().replace('&apos;',''))  # Cleans up description
		if font_text:
			desctitle.append(font_text)
		descList.append(link_desc)

for a,b,c,d in zip(titleList, hrefList, desctitle, descList):
	print(a,c,b,d,sep='\n')
import sys
import requests
import pyperclip
import bs4
import webbrowser

def start():
	search = False
	if search:
		keyword = input('Enter search term: ')
	else:
		# if no keyword is entered, the script would 
		# search for the keyword copied in the clipboard
		keyword = "Urdu OCR"


	res = requests.get('https://google.com/search?q='+keyword)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	with open(r'C:\URDU\soup.txt','w',encoding='utf8') as f:
		f.write(soup.prettify())
	#print(soup.prettify())
	# selecting class "r" and anchor tag within the class "r"
	links = soup.select('.r a')
	tab_counts = min(5, len(links))

	# for i in range(tab_counts):
	# 	webbrowser.open('https://google.com' + links[i].get('href'))


start()

import urllib
from xml.dom.minidom import parseString

def get_google_new_results( term, count ):
    results = []
    term = term.replace(' ','%20')
    url = f'http://news.google.com/news?q={term}&output=rss'
    obj = parseString( urllib.request.urlopen(url).read() )
    items = obj.getElementsByTagName('item') # Get each item
    for item in items[:count]:
        t,l = '', ''
        for node in item.childNodes:
            if node.nodeName == 'title':
                t = node.childNodes[0].data
            elif node.nodeName == 'link':
                l = node.childNodes[0].data
        results.append( (t,l) )
    return results


x = input("Enter term to scrape from")

items = get_google_new_results( x, 5 )
for title,link in items:
        print (title, '\n', link, '\n\n')
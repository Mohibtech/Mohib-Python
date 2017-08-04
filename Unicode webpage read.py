#Unicode webpage read		
import urllib.request as urlreq
 
# Copy all of the content from UrduWeb page
URL = 'http://www.urduweb.org/mehfil/threads/' + \
'%D9%BE%D8%A7%D8%A6%D8%AA%DA%BE%D9%88%D9%86-%DA%A9%D9%88%D8%B1%D8%B3-%DA%A9%DB%92-%D9%86%D8%A6%DB%92-%D9%85%D9%85%D8%A8%D8%B1%D8%A7%D9%86.59465/'
webpage = urlreq.urlopen(URL).read().decode('utf-8')
webstr = str(webpage)
print(webstr)

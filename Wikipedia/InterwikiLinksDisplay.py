# This script takes Urdu Wikipedia page and display related interwiki pages in a dictionary along with languages.
import pywikibot

site = pywikibot.Site('ur', 'wikipedia')
page = pywikibot.Page(site, u"ادیتی شرما")

langlst = page.iterlanglinks()

interDict = {}
for i in langlst:
    #lang = str(i.site).split(':')[1]
    interDict[i.site.code] = i.title
     
print(interDict)

# output of last print statement 
# {'ar': 'أديتي شارما', 'en': 'Aditi Sharma', 'gu': 'અદિતિ શર્મા', 'hi': 'अदिति शर्मा', 
# 'mr': 'आदिती शर्मा', 'pa': 'ਅਦਿਤੀ ਸ਼ਰਮਾ', 'te': 'అదితి శర్మ'}

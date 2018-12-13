# Copy Reference from English Article to Urdu Page
import pywikibot

site = pywikibot.Site()
page = pywikibot.Page(site, u"Aditi Sharma")

refdict = {}
reflinks = page.extlinks()
for i in range(10):
    refdict[i] = '<ref>' + str(next(reflinks)) + '</ref>'

for num in range(5):
    print(refdict[num]) 

site = pywikibot.Site('ur', 'wikipedia')
page = pywikibot.Page(site, u"ادیتی شرما")
#print(page.text)

# Adding Reference at the end of the page.
page.text = page.text + "\n" + refdict[3]
print(page.text)

#page.save(u"انگریزی حوالے کاپی کیے")

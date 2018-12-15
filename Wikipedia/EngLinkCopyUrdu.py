import mwparserfromhell as mwp
import pywikibot

title = "کوڈ کامبیٹ"
site = pywikibot.Site('ur', 'wikipedia')
urpage = pywikibot.Page(site, title)

langlst = urpage.iterlanglinks()

interDict = {}
for i in langlst:
    lang = str(i.site).split(':')[1]
    interDict[lang] = i.title
     
englink = interDict['en']
#print(englink)

site = pywikibot.Site('en', 'wikipedia')
enpage = pywikibot.Page(site, englink)


#reflinks = enpage.extlinks()
# k=1
# for i,link in enumerate(reflinks):
#     #i = i+1
#     refdict[i] = '<ref>' + str(link[1]) + '</ref>' # link is a tuple 

wikitext = enpage.get()               
wikicode = mwp.parse(wikitext)
# Extracting External Links using mwparserfromhell function
extlinks = wikicode.filter_external_links()

# for i in range(len(refdict)):
#     urpage.text += refdict[i] + newln

newln = '\n'
urpage.text = urpage.text + newln 

for link in extlinks:
    urpage.text += '<ref>' + str(link) + '</ref>' + newln

#urpage.text = urpage.text + str(refdict[1])
urduref = '== حوالہ جات ==' + newln + '{{حوالہ جات}}' + newln
urpage.text = urpage.text + newln*2 + urduref

print('Printing appended Urdu Page')
print(urpage.text)

urpage.save(u"انگریزی حوالے کاپی کیے")

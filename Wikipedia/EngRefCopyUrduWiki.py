# Copy Reference from English Article to Urdu Page
import mwparserfromhell as mwp
import pywikibot

title = "داس کیپیٹل"

site = pywikibot.Site('ur', 'wikipedia')
urpage = pywikibot.Page(site, title)

langlst = urpage.iterlanglinks()

interDict = {}
for i in langlst:
    lang = str(i.site).split(':')[1]
    interDict[lang] = i.title

if len(interDict)==0:
    print('Link Dictionary is empty')
else:
    englink = interDict['en']

    site = pywikibot.Site('en', 'wikipedia')
    enpage = pywikibot.Page(site, englink)

    wikitext = enpage.get()               
    wikicode = mwp.parse(wikitext)

    # Extracting External Links using mwparserfromhell function
    extlinks = wikicode.filter_external_links()

    alltags = wikicode.filter_tags()
    reftags = [tag.contents for tag in alltags if tag.tag=='ref']

    dlinks = {}
    for  i,link in enumerate(reftags):
        i+=1
        dkey = 'ح' + str(i) + 'ح'
        dlinks[dkey] = '<ref>' + str(link) + '</ref>'

    urtext = urpage.text
    for r in tuple(dlinks.items()):
        urtext = urtext.replace(*r)

    newln = '\n'

    hawalajat = '{{حوالہ جات}}'
    urduref = '== حوالہ جات ==' + newln + hawalajat + newln
    if hawalajat not in urtext:
        urpage.text = urtext + newln*2 + urduref + newln
    else:
        urpage.text = urtext + newln*2

    print('Printing appended Urdu Page')
    print(urpage.text)

    urpage.save(u"انگریزی حوالے کاپی کیے")

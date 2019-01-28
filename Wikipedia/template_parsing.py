import mwparserfromhell as mwp
import pywikibot

def search(myDict, search1):
    for key, value in myDict.items():
        if search1 in value:  
            return key

eng_title = 'Muslim conquest of Transoxiana'

site = pywikibot.Site('en', 'wikipedia')
enpage = pywikibot.Page(site, eng_title)

wikitext = enpage.get()               
wikicode = mwp.parse(wikitext)

      
sfnlist = []
for template in wikicode.filter_templates():
    if template.name in ('sfn', 'sfn'):
        #print(template.params )
        sfnlist.append(template)
        templ_rep = '<ref>' + str(template) + '</ref>'
        wikicode.replace(template , templ_rep)

alltags = wikicode.filter_tags()
reftags = {}

i=1
for tag in alltags:
    if tag.tag=='ref':
        if tag.attributes == []:      #check if attributes list is empty
            refval='NoRefName'
        else:
            name = tag.attributes[0]
            refval = name.value
            
        if tag.contents is None:
            pass
        else:    
            reftags[i] = (refval,tag.contents)
            print(reftags[i])
            i += 1

for ref in reftags:
    print(ref)

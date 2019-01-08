# Extracting Infobox template in a dictionary

import mwparserfromhell as mwp
import pywikibot

title = "Vyasa"

site = pywikibot.Site('en', 'wikipedia')
page = pywikibot.Page(site, title)

wikitext = page.get()
wikicode = mwp.parse(wikitext)

sfnlist = []
templbox = {}
infobox= {}

for template in wikicode.filter_templates():
    tname = template.name
    tparams = template.params
    if 'Infobox' in tname:
        for param in tparams:
            pname, valstr = param.name.strip(), param.value.strip() 
            #pname, valstr = param.split('=') 
            infobox[pname] = valstr

print(infobox)

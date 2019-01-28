import mwparserfromhell as mwp
import pywikibot
import noreferences

def search(myDict, search1):
    for key, value in myDict.items():
        if search1 in value:  
            return key


#
# title = "پھیرن"
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
    eng_title = interDict['en']

    site = pywikibot.Site('en', 'wikipedia')
    enpage = pywikibot.Page(site, eng_title)

    wikitext = enpage.get()               
    wikicode = mwp.parse(wikitext)

    # Extracting External Links using mwparserfromhell function
    #extlinks = wikicode.filter_external_links()

    alltags = wikicode.filter_tags()
    reftags = {}
    #[tag.contents for tag in alltags if tag.tag=='ref']
      
    i=1
    for tag in alltags:
        if tag.tag=='ref':
            if tag.attributes == []:      #check if attributes list is empty
                refval='NoRefName'
            else:
                name = tag.attributes[0]
                refval = name.value
                
            if tag.contents is None:
                #conval = search(reftags,refval)
                #reftags[i] = (refval,reftags[conval][1])
                pass
            else:    
                reftags[i] = (refval,tag.contents)
                i += 1

    dlinks = {}
    for k,v in reftags.items():
        dkey = 'و' + str(k) + 'و'
        dlinks[dkey] = '<ref>' + str(v[1]) + '</ref>'

    urtext = urpage.text
    for r in tuple(dlinks.items()):
        urtext = urtext.replace(*r)

    # newln = '\n'
    # hawalajat = '{{حوالہ جات}}'
    # urduref = '== حوالہ جات ==' + newln + hawalajat + newln
    # if hawalajat not in urtext:
    #     urpage.text = urtext + newln*2 + urduref + newln
    # else:
    #     urpage.text = urtext + newln*2        

    # Recommended by Shoaib
    #hawalajat = '{{حوالہ جات}}'
    #if hawalajat not in urtext:
    norefbot = noreferences.NoReferencesBot(None)
    if norefbot.lacksReferences(urtext):
        newtext = norefbot.addReferences(urtext)
    else:
        urpage.text = urtext + '\n'
    #urpage.text = urtext + '\n'

    print('Printing appended Urdu Page')
    #print(urpage.text)
    print(newtext)
    # save the page
    #urpage.save(summary=self.summary, minor=False)


  
    

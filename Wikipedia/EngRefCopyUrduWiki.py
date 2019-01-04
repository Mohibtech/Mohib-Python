# Copy Reference from English Article to Urdu Pageimport mwparserfromhell as mwp
import pywikibot
from scripts import noreferences

def search(myDict, search1):
    for key, value in myDict.items():
        if search1 in value:  
            return key

title = "متحدہ حزب اختلاف (بھارت)" 

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

    # Extracting sfn templates and converting them in REF tags
    sfnlist = []
    for template in wikicode.filter_templates():
        if template.name in ('sfn', 'sfn'):
            sfnlist.append(template)
            templ_rep = '<ref>' + str(template) + '</ref>'
            wikicode.replace(template , templ_rep)


    alltags = wikicode.filter_tags()
    reftags = {}
    refdict = {}
    #[tag.contents for tag in alltags if tag.tag=='ref']
      
    i=1
    for tag in alltags:
        if tag.tag=='ref':
            if tag.attributes == []:      #check if attributes list is empty
                refname='NoRefName'
            else:
                name = tag.attributes[0]  # tag.attributes[0] is reference name
                refname = str(name.value)
                
            if tag.contents is None:
                refval = refdict.get(refname,'noval')
                if refval == 'noval':
                    refdict[refname] = i
                    reftags[i] = (refname,refval)
                    i += 1 
                else:
                    if refdict[refname]:
                        pass
                        #i += 1 #increment the key to indicate that a valid reference added in dict

                #refkey = search(reftags,refname)
                #reftags[i] = (refval,reftags[refkey][1])
            else:
                if refname in refdict:
                    ival = refdict[refname]
                    reftags[ival] = (refname,tag.contents)
                else:
                    reftags[i] = (refname,tag.contents)
                    if refname != 'NoRefName':
                        refdict[refname] = i
                    i += 1
                #print(reftags[i])
                

    dlinks = {}
    for k,v in reftags.items():
        dkey = 'و' + str(k) + 'و'
        reftext = str(v[1])
        dlinks[dkey] = '<ref>' + reftext + '</ref>'

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
    
    # Used noreferences to add Reference List in Article
    norefbot = noreferences.NoReferencesBot(None)
    if norefbot.lacksReferences(urtext):
        urtext = norefbot.addReferences(urtext)
    else:
        urpage.text = urtext + '\n'
    
    print('Printing appended Urdu Page')
    print(urpage.text)

    # save the page
    #urpage.save(summary=self.summary, minor=False)


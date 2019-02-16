#!/data/project/mohib/www/python/venv/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import cgi
import urllib
from subprocess import Popen, PIPE
import logging
import mwparserfromhell as mwp
import pywikibot


#FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
logging.basicConfig(filename='/data/project/mohib/public_html/debug.log',
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

logging.info('Logging started before Web page')

print("Content-Type: text/html")

print( """<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
<title>Provide Title for Copying</title> 
</head>

<body>
<div>
<a href="index.html">New search</a>
<br><br> 
""" )

try:
    form = cgi.FieldStorage()

    if "page" in form:
        pagetitle = form.getvalue('page')
                  
    heading2 = '<h2> Page Title => {} </h2>'.format(pagetitle)
    print(heading2)
    print( '<form action="title.py" method="get">' ) 
    print( """<input type="submit" value="Submit" /> </form> """ )
    
    print("<b>Trying to copy Links</b>")
    
    logging.debug('Page Title => {}'.format(pagetitle))

    venv = Popen(['sh','source','/data/project/mohib/www/python/venv/bin/activate'])
    site = pywikibot.Site('ur', 'wikipedia')
    urpage = pywikibot.Page(site, pagetitle)

    logging.debug('Getting Urdu Page from Wikipedia => {}'.format(urpage.text[0:5]))
    print('<h2> Reference Links copied </h2>')
    print("</div>\n</BODY>\n</HTML>")

except Exception as e:
    logging.exception("Exception occurred")

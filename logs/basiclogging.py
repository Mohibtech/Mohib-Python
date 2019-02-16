#!/data/project/mohib/www/python/venv/bin/python
# # -*- coding: utf-8 -*-

import sys
import os
import cgi
import urllib
from subprocess import Popen, PIPE
import shlex
import logging


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
    
    # f =  open('test.txt','w')
    # f.write(pagetitle)
    
    logging.debug('Page Title => {}'.format(pagetitle))

    kwargs = {}
    kwargs['stdout'] = PIPE
    kwargs['stderr'] = PIPE
    
    pythonpath = r'/data/project/mohib/www/python/venv/bin/python'
    pwb = r'/data/project/mohib/core/pwb.py'
    hawala = r'/data/project/mohib/core/copyLinks.py'
    argtitle = '-page:' + pagetitle

    venv = Popen(['sh','source','/data/project/mohib/www/python/venv/bin/activate'])
    pwbresult = Popen(['python', '/data/project/mohib/core/pwb.py','login'])

    result = Popen(['python','/data/project/mohib/core/copyLinks.py',argtitle],shell=True, **kwargs)

     
    logging.info('Waiting for few moments................')
    result.wait()
    stdout, stderr = result.communicate()

    if stdout:
        for line in stdout.strip().split("\n"):
            logging.info(line)

    if stderr:
        for line in stderr.strip().split("\n"):
            logging.error(line)

    print('<h2> Reference Links copied </h2>')
    print("</div>\n</BODY>\n</HTML>")

except Exception as e:
    logging.exception("Exception occurred")

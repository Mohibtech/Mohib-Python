import re

PATTERN = re.compile(r'(?P<city>[A-Z][\w\s]+?).(?P<state>TX|OR|OH|MN)')
TEXT ='the jackalopes are the team of Odessa,TX while the knights are native of Corvallis OR and the mud hens come from Toledo.OH; the whitecaps have their base in Grand Rapids,MI'
match = PATTERN.search(TEXT)
 
match.group(2)
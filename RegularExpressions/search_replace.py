import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

#For more complicated substitutions, it’s possible to specify a substitution callback function instead.
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat.sub(change_date, text)
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'

# If you want to know how many substitutions were made in addition to getting replacement text, 
# use re.subn() instead.
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n,sep='####')
# 'Today is 2012-11-27. PyCon starts 2013-3-13. ###2'



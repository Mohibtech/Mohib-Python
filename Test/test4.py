import re
#template : 422XX-47XXXX4-1
instr =  '42211-4756564-11'

if re.match(r'\d{3}\w{2}-\d{2}\w{4}\d-\d{1}', instr):
	print('Template matched')
else:
	print('Template match failed')


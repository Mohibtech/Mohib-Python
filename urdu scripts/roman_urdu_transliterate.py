import codecs
import os
import re

def dict_populate(FILE_NAME):
	try:
		if os.path.isfile(FILE_NAME):
			store = open(FILE_NAME,'r',encoding='utf-8')
		for line in store.readlines():
			eng,urdu = line.strip().split(':',1)
			roman_urdu[eng] = urdu
	except ValueError as e:
		print(e)

def multiwordReplace(text, wordDic):
	"""
	take a text and replace words that match a key in a dictionary with
	the associated value, return the changed text
	"""
	# r'\b'+r'\b|\b'
	rc = re.compile(r'\b|\b'.join(map(re.escape, wordDic)))

	def translate(match):
		return wordDic[match.group(0)]
	return rc.sub(translate, text)

#H:\BACKUP\Python
basedir = os.path.join("H:",os.sep,"Backup","Python","MISC","urduscripts")
dict_file = os.path.join(basedir,"dict.txt")
input_file = os.path.join(basedir,"input.txt")
output_file = os.path.join(basedir,"output.txt")
roman_urdu = {}

#Populate the dictionary with Roman(keys) and Urdu(values) words
dict_populate(dict_file)

f = open(input_file,'r')
data = f.read()
f.close()

text = multiwordReplace(data, roman_urdu)

# write the whole file result
f = open(output_file,'w',encoding='utf-8')
f.write(text)
f.close()

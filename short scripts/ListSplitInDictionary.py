# Splitting List into a dictionary while stripping unwanted characters like '[[' and ']]'
lst = ['[[en:Aditi Sharma]]','[[ur:ادیتی شرما]]','[[ar:أديتي شارما]]']

# Stripping '[[]]' from list element and then split the element based on character ':' to 
# form a dictionary element based on language code and related  
langdict  = dict(i.strip('[[]]').split(':') for i in lst)
print(langdict)

# Output
{'en': 'Aditi Sharma', 'ur': 'ادیتی شرما', 'ar': 'أديتي شارما'}

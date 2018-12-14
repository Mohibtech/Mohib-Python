# Splitting List into a dictionary while stripping unwanted characters like '[[' and ']]'
lst = ['[[ur:ادیتی شرما]]','[[ar:أديتي شارما]]']

langdict  = dict(i.strip('[[]]').split(':') for i in lst)
print(langdict)

# Output
# {'ur': 'ادیتی شرما', 'ar': 'أديتي شارما'}

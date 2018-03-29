import re

ingredient = "Kumquat: 2 cups"
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'

pattern = re.compile(pattern_text)

match = pattern.match(ingredient)

print( match.groups() )

print( match.group('ingredient') )
print( match.group('amount') )
print( match.group('unit') )

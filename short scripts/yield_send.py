def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]


mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']
shortstringlist = shorten(mystringlist)
result = []
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        # using sum for calculating the length of vowels in string s, no len function for filter object
        number_of_vowels = sum(1 for _ in filter(lambda letter: letter in 'aeiou', s))
        # Truncate the next string depending on number of vowels in the previous one
        a = shortstringlist.send(number_of_vowels)
        result.append(a)
        print(result)
except StopIteration:
    pass
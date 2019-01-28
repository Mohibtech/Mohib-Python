#textfile1 = r'D:\script\MohibPython\Mohib-Python\Test\poem.txt'
textfile = r'D:\script\test\poem.txt'

fpoem = open(textfile)
fpoem.close()

with open(textfile) as fpoem:
    result = fpoem.read()
    print(result)

results = []

with open(textfile) as fpoem:
    results = fpoem.readlines()



#write method for writing single line to a file
quotes = r'D:\script\test\quotes.txt'
with open(quotes,'w') as fq:
    fq.write('Before God we are all equally wise - and equally foolish.')
    fq.write('I never teach my pupils. I only attempt to provide the conditions in which they can learn.')


Einstein = ['I never think of the future - it comes soon enough.',
'It is a miracle that curiosity survives formal education.',
'It is the supreme art of the teacher to awaken joy in creative expression and knowledge.']

with open(quotes,'w') as fq:
    fq.writelines(line+'\n' for line in Einstein)
    fq.writelines()







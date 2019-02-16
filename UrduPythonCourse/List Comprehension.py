'''
List comprehensions provide a concise way to create lists. 
It consists of brackets containing an expression followed by a for clause, then
optional if clauses. 
The expressions can be anything, meaning you can put in all kinds of objects in lists.
The list comprehension always returns a result list.
'''

# List comprehensions in Python are constructed as follows:

list_variable = [x for x in sequence]

# In maths, common ways to describe lists (or sets, or tuples, or vectors) are:
'''
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}
'''

'''
sequence S contains values between 0 and 9 included that are raised to the power of two.
Sequence V contains the value 2 that is raised to a certain power. 
For the first element in the sequence, this is 0, for the second this is 1, and so on, until you reach 12.
sequence M contains elements from the sequence S, but only the even ones.
'''
# Above mathematical expressions will produce following lists.
S = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
V = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}
M = {0, 4, 16, 36, 64}

# Creating List S using List comprehension
S = [x**2 for x in range(10)]

# Creating List S using for Loop
S = []
for x in range(10):
    S.append(x**2)

# Creating List V using List comprehension
V = [2**i for i in range(13)]

# Creating List V using for Loop
V = []
for i in range(13):
    V.append(2**i)

# Creating List M using List comprehension
M = [x for x in S if x % 2 == 0]

# Creating List M using for Loop
M = []
for x in S:
    if x % 2 ==0:
        M.append(x)


# Celsius to Fahrenheit conversion
Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit = [((9/5)*x + 32) for x in Celsius ]
print(Fahrenheit)

# Celsius to Fahrenheit using for loop
Fahrenheit = []
for x in Celsius:
    item = (9/5)*x + 32
    Fahrenheit.append(item)

# Transpose matrix
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]

print (transpose)

matrix = [[1, 2], [3,4], [5,6], [7,8]]

# Transpose matrix using for Loop
transposed = []
for i in range(2):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
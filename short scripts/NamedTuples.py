from collections import namedtuple

Person = namedtuple('Person', 'name age')

perry = Person(name="Perry", age=30)

# Without specifying the field names in NamedTuple
jane = Person("Jane", 35)

#people = [('John', 30), ('Peter', 28), ('Joe', 42)]
Persons = [perry, jane]

sortPerson = sorted(Persons, key=lambda p: p.age) 

print( [(person.name,person.age) for person in Persons if person.age > 30] )




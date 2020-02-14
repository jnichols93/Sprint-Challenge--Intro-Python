# The following list comprehension exercises will make use of the 
# defined Human class. 
import math
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
# https://www.daniweb.com/programming/software-development/code/216631/a-list-of-class-objects-python
# i is not iterable?
a = [human.name for human in humans if human.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [human.name for human in humans if human.name[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
chars = set('CDEFG')
c = [human.name for human in humans if 'C' in human.name[0] or 'D' in human.name[0]
    or 'E' in human.name[0] or 'F' in human.name[0] or 'G' in human.name[0]]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [(int(human.age) + 10) for human in humans]
print(d)
# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{human.name}-{human.age}" for human in humans]
print(e)
# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name, human.age)
    for human in humans if human.age >= 27 and human.age <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase and added 5 years to age:")
g = [Human(human.name.upper(), (human.age + 5)) for human in humans]
print(g)
print('old humans list:', humans)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [(math.sqrt(human.age)) for human in humans]
print(h)
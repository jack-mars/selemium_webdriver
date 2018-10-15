"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""
print(list(range(0, 10)))
a = range(0, 20, 3)
print(a)
print(type(a))
print(list(a))
for num in range(0, 10, 3):
    print(num)


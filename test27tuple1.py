"""
tuple is like list but imnutable
"""

my_list = [1, 2, 3, 6, 8,10]
print(my_list)
my_list[0] = 0
print(my_list)
my_tuple = (1, 2, 2, 3, 2, 5, 4, 5, 8, 9, 9)
print(my_tuple[0])
print(my_tuple[5:])
print("*"*20)
print(my_tuple.index(2))
print(my_tuple.count(2))
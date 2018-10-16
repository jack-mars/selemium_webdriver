"""
Iterating multiple lists at the same time
"""
a1 =[1, 8, 9]
a2 =[2, 6, 10, 12,15]
for a, b in zip(a1, a2):
    if a > b:
        print(a)
    else:
        print(b)
for a, b in zip(a1, a2):
    print(a)
    print(b)
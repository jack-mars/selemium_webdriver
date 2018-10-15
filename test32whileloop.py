"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Itrrable items are Strings,List,Tuple,Dictionary
"""
x = 0
while x < 5:
    print("value of x is: " + str(x))
    x += 1

a = []
num = 0
while num < 4:
    a.append(num)
    print("value of num is " + str(num) )
    num += 1
print(a)
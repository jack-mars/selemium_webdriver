"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Itrrable items are Strings,List,Tuple,Dictionary
"""
#string for loop
my_string = "abcabc"
for c in my_string:
    #print(c)
    print(c, end = " ")
print()
#list for loop
cars = ["bmw", "bens", "honda"]
for car in cars:
    print(car)
nums = [1, 2, 3]
for n in nums:
    print("*"*10)
print("*"*20)
#dictionary for loop
d = {"one": 1, "two": 2, "three": 3}
for k in d:
    print(k + " " + str(d[k]))
print("*"*20)
for k,v in d.items():
    print(k)
    print(v)


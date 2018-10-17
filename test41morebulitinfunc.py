"""
Some built-in functions
max(): It takes any number of arguments and return the largest one.
min(): It takes any number of arguments anf return the smallest one.
obs(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.
type(): It returns the type of the data it receives an an argument.

"""
def largest_num(*args):
    print(max(args))
    return(max(args))
largest_num(-20, -10, 10, 100)

def smallest_num(*args):
    print(min(args))
smallest_num(-20, -10, 10, 100)
print("*"*20)
def abs_function(a):
    print(abs(a))
abs_function(-8)
abs_function(8)
print(type(99))
print(type(99.99))
print(type("99.99"))


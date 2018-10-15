"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""
x = 0
while x < 6:
    print("value of x is: " + str(x))
    x += 1
    #if x ==4:
        #break
    print("This example is awesome")
    print("*#"*20)
    print("circle again")
else:
    print("broke out of the loop")

# x = 0
# while x < 7:
#     print("value of x is: " + str(x))
#     x += 1
#     if x ==4:
#         continue
#     print("This example is awesome")
#     print("*#"*20)
#     print("circle again")
# print("game over")
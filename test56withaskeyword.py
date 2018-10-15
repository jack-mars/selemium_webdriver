"""
With As Keywords
"""
print("Normal Write Start")
my_write = open("testfile2.txt", "w")
my_write.write("Tring to write to the file")
my_write.close()
print("*"*20)

print("Normal Read Start")
my_read = open("testfile2.txt", "r")
print(str(my_read.read()))
print("*"*20)

print("With As Write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("this is an example of with as write/read")
print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))
print("*"*20)


with open("withas.txt", "w") as with_as_write:
    with_as_write.write("this is an example of with as write/read,second sentence")
print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))

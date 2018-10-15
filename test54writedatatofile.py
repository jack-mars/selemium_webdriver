"""
File I/O
"w" ---> Write-only Mode
"r" ----> Read-only Mode
"r+" --->Read And Write Mode
"a" --->Append Mode
"""
my_list = [1, 2, 3]
my_life = open("firstfile.txt", "w")

for item in my_list:
    my_life.write(str(item) + "\n")

my_life.close()
def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2
sum1 = sum_nums(2, 8)
print(sum1)
print("*"*20)
def isMetro(city):
    l = ["sfo", "nyc", "boston"]
    if city in l:
        return True
    else:
        return False
x = isMetro("boston")
print(x)
string_add = sum_nums("one", "two")
print(string_add)
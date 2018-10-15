#test
a = [1, 2, 3, 2, 4, 2]
print(a.count(2))

#Data type to store more than one value in one variable mame, in terms of key value pairs
#Dictionary items are in brackets {} in key: value pairs, separated with "," {"k1":"v1", "k2":"v2"}
#Not sequenced, no indexing--->Mapping
car = {"make": "bmw", "model": "750i", "year": "2016", "color": "blue"}
print(car)
print(car["year"])
model = car["model"]
print(model)
d = {}
d["one"] = 1
d["two"] = 2
print(d)
sum_1 = d["two"] + 8
print(sum_1)
print(d)
d["two"] = d["two"] + 8
print(d)
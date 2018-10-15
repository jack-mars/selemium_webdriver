"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
import testCar as car
from testCar import info
class ModulesDemo():
    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))
    def car(self):
        make = "bmw"
        model = "550i"
        car.info(make, model)
        info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car()
"""
Objected Oriented Programming
"""
class Car(object):
    def __init__(self, make, model='550i'):
        self.yumake = make
        self.model = model
c1= Car('bmw')
print(c1.yumake)
print(c1.model)
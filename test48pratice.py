class Fruit(object):
    def __init__(self):
        print("I am a fruit")
    def nutriton(self):
        print("I am full of vitamins")
    def fruit_shape(self):
        print("Every fruit can have different shape")
class Orange(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("I am a orange")
    def nutriton(self):
        print("I am full of vitamin ")
    def color(self):
        print("the color is yellow")
a = Fruit()
a.fruit_shape()
a.nutriton()
b = Orange()
b.nutriton()
b.fruit_shape()
b.color()
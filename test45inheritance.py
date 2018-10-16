class Car(object):
    def __init__(self):
        print("you just created the car instance")
    def drive(self):
        print("Car started....")
    def stop(self):
        print("Car stopped")
class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print("you just create a BMW")

c = Car()
c.drive()
c.stop()
b = BMW()
b.drive()
b.stop()
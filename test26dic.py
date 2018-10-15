#Dictionary methods
cars = {"bmw": {"model": "750i", "year": "2016"}, "benz": {"model": "e600", "year": "2018"}}
car = {"make": "bmw", "model": "550", "year": "2016"}
print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())
car_copy = car.copy()
print(car_copy)
print(car.pop("model"))
print(car)
car.clear()
print(car)
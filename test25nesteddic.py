"""
Nested Dictionary:
d = {"k1": {"nestk1":"nestvalue", "nestk2":"nestvalue"}}
d["k1"]["nestk1"]
"""
cars = {"bmw": {"model": "750i", "year": "2016"}, "benz": {"model": "e600", "year": "2018"}}
bmw_year = cars ["bmw"]["year"]
print(bmw_year)
print(cars["benz"]["model"])
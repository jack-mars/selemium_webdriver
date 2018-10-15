#Exception practise
def exceptionhandling():
    try:
        car = {"make": "bmw", "model": "550i", "yesr": "2016"}
        print(car["color"])
    except:
        print("key not found")
    finally:
        print("please try a different key")
exceptionhandling()
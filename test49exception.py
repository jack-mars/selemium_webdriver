#ExceptionHandling
def exceptionHandling():
    try:
        a = 10
        b = 5
        c = 0
        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("Zero Division")
    except TypeError:
        print("Cant add string to integer")
    #except:
        #print("In the except block")
exceptionHandling()
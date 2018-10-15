#Finally and Else block
#ExceptionHandling
def exceptionHandling():
    try:
        a = 10
        b = 5
        c = 0
        d = (a + b) / c
        print(d)
    except:
        print("In the except block")
        #show the exception name
        raise Exception("this is on exception")
    else:
        print("there was no exception, else is executed")
    finally:
        print("Finally, always executed")
exceptionHandling()
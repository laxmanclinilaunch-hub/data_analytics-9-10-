
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ValueError("can't divide with zero")
    return x/y
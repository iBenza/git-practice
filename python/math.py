def negative(x):
    return -x

def power(x, y):
    return x ** y

def absolute(x):
    if x < 0:
        return negative(x)
    else:
        return x

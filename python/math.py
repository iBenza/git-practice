def negative(x):
    return -x

def power(x, y):
    return x ** y

def absolute(x):
    return -x if x < 0 else x

def is_odd(x):
    return x % 2 == 0

def is_even(x):
    return is_odd(x-1)

def rectangle(x, y):
    return x * y

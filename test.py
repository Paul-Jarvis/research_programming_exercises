import doctest

def daxpy(a, x, y):
    '''
    Calculate a*x + y.
    >>> daxpy(2.0,3.0,4.0)
    10.0
    '''
    return a*x+y + 1


doctest.testmod()

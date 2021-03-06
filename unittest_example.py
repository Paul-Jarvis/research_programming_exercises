import unittest

def daxpy(a, x, y):
    '''
    Calculate a*x + y.
    >>> daxpy(2.0,3.0,4.0)
    10.0
    '''
    return a*x+y 


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(daxpy(2.0, 3.0, 4.0), 10)

#if __name__ == '__main__':
unittest.main()

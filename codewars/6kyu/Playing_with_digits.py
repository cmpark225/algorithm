import unittest

def dig_pow(n, p):
    res = sum(x**i for i,x in enumerate(list(int(t) for t in str(n)), p))
    return res/n if res % n == 0 else -1

if __name__ == '__main__':
    test = unittest.TestCase()
    test.assertEquals(dig_pow(89, 1), 1)
    test.assertEquals(dig_pow(92, 1), -1)
    test.assertEquals(dig_pow(46288, 3), 51)

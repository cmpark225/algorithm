import unittest
from functools import reduce

def unique_in_order(a):
    def func(x, y):
        if type(x) is not list:
            x = [x,]
        if x[len(x)-1] != y:
            x.append(y)
        return x
    print (a)
    return reduce(func, a)

from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]



if __name__ == '__main__':
    test = unittest.TestCase()
    test.assertEquals(unique_in_order('A'), ['A'])
    # test.assertEquals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
    # test.assertEquals(unique_in_order([1,2,3,3]),[1,2,3])

import unittest

def order(sentence):
  return ' '.join(sorted(sentence.split(' '), key=lambda word: filter(lambda x: x.isdigit(), word)))

if __name__ == '__main__':
    Test = unittest.TestCase()
    Test.assertEquals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
    Test.assertEquals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
    Test.assertEquals(order(""), "")

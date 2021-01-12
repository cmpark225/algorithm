import unittest

def duplicate_encode(word):
    return ''.join(')' if word.lower().count(x.lower()) > 1 else '(' for x in word)


if __name__ == '__main__':
    Test = unittest.TestCase()

    Test.assertEquals(duplicate_encode("din"),"(((")
    Test.assertEquals(duplicate_encode("recede"),"()()()")
    Test.assertEquals(duplicate_encode("Success"),")())())","should ignore case")
    Test.assertEquals(duplicate_encode("(( @"),"))((")

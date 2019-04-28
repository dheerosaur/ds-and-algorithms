import math
from nose.tools import assert_equal


def is_palindrome(x):
    "Decimal palindrome check"
    n = math.floor(math.log10(x))
    mask = 10 ** n
    while mask > 1:
        if (x // mask) != (x % 10):
            return False
        x = (x % mask) // 10
        mask = mask // 100
    return True


class TestBit(object):

    def test_is_palindrome(self, is_palindrome_f):
        assert_equal(is_palindrome_f(12345), False)
        assert_equal(is_palindrome_f(2324), False)
        assert_equal(is_palindrome_f(12321), True)
        assert_equal(is_palindrome_f(111222111), True)
        print('Success: {}'.format(is_palindrome_f.__name__))


def main():
    test = TestBit()
    test.test_is_palindrome(is_palindrome)


if __name__ == '__main__':
    main()

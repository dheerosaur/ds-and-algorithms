"""
Compute the parity of a very large number of 64-bit words
Brute-force algorithm iterates over each bit
"""
from nose.tools import assert_equal


def count_bits(x):
    count = 0
    while x:
        count += 1
        x = x & (x - 1)
    return count


def parity(x):
    result = 0
    while x:
        result ^= 1
        x = x & (x - 1)
    return result


def parity_bf(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


class TestBit(object):

    def test_count(self, count_f):
        a = int('1000010000111101' * 3, base=2)
        b = int('0000000000010011' * 6, base=2)
        assert_equal(count_f(a), 21)
        assert_equal(count_f(b), 18)
        print('Success: {}'.format(count_f.__name__))

    def test_parity(self, parity_f):
        a = int('1000010000111101' * 3, base=2)
        b = int('0000000000010011' * 6, base=2)
        assert_equal(parity_f(a), 1)
        assert_equal(parity_f(b), 0)
        print('Success: {}'.format(parity_f.__name__))


def main():
    test = TestBit()
    test.test_parity(parity_bf)
    test.test_parity(parity)
    test.test_count(count_bits)
    test.test_count(count_bits)


if __name__ == '__main__':
    main()

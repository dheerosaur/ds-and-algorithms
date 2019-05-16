"""
Swap ith bit with jth
"""
from nose.tools import assert_equal


def swap_bits(x, i, j):
    # Extract the i-th and j-th and compare to see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        # Create a mask with 1 shifted to i-th and j-th positions
        # Use this mask to flip the bits at these exact locations
        mask = (1 << i) | (1 << j)
        x = x ^ mask
    return x


def swap_naive(x, i, j):
    # Get i_val and j_val
    i_val = (x >> i) & 1
    j_val = (x >> j) & 1
    if i_val != j_val:
        # create a mask with zeroes at i and j
        mask = ~((1 << i) | (1 << j))
        # Clear bits at i and j, then set values there
        x = (x & mask) | (i_val << j) | (j_val << i)
    return x


class TestBit(object):

    def test_count(self, count_f):
        a = int('1000010000111101' * 3, base=2)
        b = int('0000000000010011' * 6, base=2)
        assert_equal(count_f(a), 21)
        assert_equal(count_f(b), 18)
        print('Success: {}'.format(count_f.__name__))

    def test_swap(self, swap_f):
        a = int('1000010000111101', base=2)
        expected = int('1000010000111011', base=2)
        assert_equal(swap_f(a, 1, 2), expected)
        b = int('0000000000010011', base=2)
        expected = int('0001000000000011', base=2)
        assert_equal(swap_f(b, 4, 12), expected)
        print('Success: {}'.format(swap_f.__name__))


def main():
    test = TestBit()
    test.test_swap(swap_naive)
    test.test_swap(swap_bits)


if __name__ == '__main__':
    main()

"""
Pairwise swap numbers
"""
from nose.tools import assert_equal


def pairwise_swap(B):
    return (
        ((B & 0xaaaaaa) >> 1) |
        ((B & 0x555555) << 1)
    )


class Test(object):

    def test_pairwise_swap(self, f):
        assert_equal(f(0b10101010), 0b01010101)
        assert_equal(f(0b10001000), 0b01000100)
        print('Success: {}'.format(f.__name__))


def main():
    test = Test()
    test.test_pairwise_swap(pairwise_swap)


if __name__ == '__main__':
    main()

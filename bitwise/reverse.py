from nose.tools import assert_equal


def print_binary(n):
    print('{0:032b}'.format(n))


def rev(n):
    answer = 0
    for i in range(16):
        answer = (answer << 1) | ((n >> i) & 1)
    return answer


class TestBit(object):

    def test_rev(self, rev_f):
        a = int('1000010000111101', base=2)
        expected = int('1011110000100001', base=2)
        assert_equal(rev_f(a), expected)
        b = int('0000000000010011', base=2)
        expected = int('1100100000000000', base=2)
        assert_equal(rev_f(b), expected)
        c = 0xffff
        expected = 0xffff
        assert_equal(rev_f(c), expected)
        print('Success: {}'.format(rev_f.__name__))


def main():
    test = TestBit()
    test.test_rev(rev)


if __name__ == '__main__':
    main()

from nose.tools import assert_equal


def print_hex(*args):
    print(' '.join('{0:x}'.format(x) for x in args))


def reverse_any(x, base):
    result, cp = 0, x
    while cp > 0:
        result = result * base + cp % base
        cp //= base
    return result


class TestBit(object):

    def test_reverse_any(self, reverse_any_f):
        assert_equal(reverse_any_f(0xabcd, 16), 0xdcba)
        assert_equal(reverse_any_f(0o767, 8), 0o767)
        assert_equal(reverse_any_f(1234, 10), 4321)
        print('Success: {}'.format(reverse_any_f.__name__))


def main():
    test = TestBit()
    test.test_reverse_any(reverse_any)


if __name__ == '__main__':
    main()

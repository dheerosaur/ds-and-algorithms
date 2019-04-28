from nose.tools import assert_equal


def print_binary(*args):
    print(' '.join('{0:016b}'.format(x) for x in args))


def raised_to_alt(x, y):
    result = 1.0
    if y < 0:
        x, y = 1.0 / x, -y
    while y > 0:
        if y & 1:
            result *= x
        y >>= 1
        x *= x
    return result


def raised_to(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


class TestBit(object):

    def test_raised_to(self, raised_to_f):
        assert_equal(raised_to_f(2, 6), 2.0 ** 6)
        assert_equal(raised_to_f(3, 5), 3.0 ** 5)
        assert_equal(raised_to_f(2, -5), 2.0 ** -5)
        print('Success: {}'.format(raised_to_f.__name__))


def main():
    test = TestBit()
    test.test_raised_to(raised_to)
    test.test_raised_to(raised_to_alt)


if __name__ == '__main__':
    main()

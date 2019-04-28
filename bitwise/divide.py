from nose.tools import assert_equal


def print_binary(*args):
    print(' '.join('{0:016b}'.format(x) for x in args))


def divide_iter(x, y):
    result, power = 0, 0
    y2n = y
    while x >= y:
        while (y2n << 1) < x:
            y2n <<= 1
            power += 1
        result += (1 << power)
        x, y2n, power = x - y2n, y, 0
    return result


def divide_rev(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result


def divide_simple(x, y):
    return x // y


class TestBit(object):

    def test_divide(self, divide_f):
        assert_equal(divide_f(2000, 4), 500)
        assert_equal(divide_f(213213212, 99887), 2134)
        print('Success: {}'.format(divide_f.__name__))


def main():
    test = TestBit()
    test.test_divide(divide_simple)
    test.test_divide(divide_iter)
    test.test_divide(divide_rev)


if __name__ == '__main__':
    main()

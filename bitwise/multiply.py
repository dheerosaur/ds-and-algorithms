from nose.tools import assert_equal


def print_binary(*args):
    print(' '.join('{0:016b}'.format(x) for x in args))


def multiply(x, y):
    def add(a, b):
        total, carry, mask = 0, 0, 1
        while a or b:
            ak, bk = a & 1, b & 1
            col_sum = ak ^ bk ^ carry
            carry = (ak & bk) | (ak & carry) | (bk & carry)
            total = (total | mask) if col_sum else total
            a, b, mask = a >> 1, b >> 1, mask << 1
        total = (total | mask) if carry else total
        return total

    result = 0
    while y > 0:
        if (y & 1):
            result = add(result, x)
        x, y = x << 1, y >> 1
    return result


class TestBit(object):

    def test_multiply(self, multiply_f):
        assert_equal(multiply_f(1, 1), 1)
        assert_equal(multiply_f(2, 4), 8)
        assert_equal(multiply_f(12, 13), 156)
        assert_equal(multiply_f(22123, 9876), 218486748)
        print('Success: {}'.format(multiply_f.__name__))


def main():
    test = TestBit()
    test.test_multiply(multiply)


if __name__ == '__main__':
    main()

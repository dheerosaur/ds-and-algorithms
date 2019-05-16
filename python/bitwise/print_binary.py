from nose.tools import assert_equal


class Bits(object):

    def print_binary(self, num):
        if num is None or num in (0, 1):
            return 'ERROR'
        ans = ['0.']
        cp = num
        while cp > 0:
            if cp * 2 >= 1:
                ans.append('1')
                cp = cp * 2 - 1
            else:
                ans.append('0')
                cp = cp * 2
            if len(ans) > 32:
                return 'ERROR'
        return(''.join(ans))


class TestBits(object):

    def test_print_binary(self):
        bit = Bits()
        assert_equal(bit.print_binary(None), 'ERROR')
        assert_equal(bit.print_binary(0), 'ERROR')
        assert_equal(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        assert_equal(bit.print_binary(num), expected)
        num = 0.6875
        expected = '0.1011'
        assert_equal(bit.print_binary(num), expected)
        num = 0.987654321
        assert_equal(bit.print_binary(num), 'ERROR')
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_print_binary()


if __name__ == '__main__':
    main()

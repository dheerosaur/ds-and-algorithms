from nose.tools import assert_equal, assert_raises


class Bits(object):

    def flip_bit(self, num):
        if num is None:
            raise TypeError
        mx = 0
        ones = 0
        counter = 0
        zero1, zero2, zero3 = 0, 0, 0
        while num > 0:
            counter += 1
            if (num >> 1) & 1 == 0:
                ones = 0
                print(zero3 - zero1, zero2 - zero1, mx, ones)
                mx = max(zero3 - zero1, zero2 - zero1, mx, ones)
            else:
                ones += 1
            num = num >> 1
        return mx + 1


class TestBits(object):

    def test_flip_bit(self):
        bits = Bits()
        assert_raises(TypeError, bits.flip_bit, None)
        assert_equal(bits.flip_bit(0), 1)
        # assert_equal(bits.flip_bit(-1), bits.MAX_BITS)
        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        assert_equal(bits.flip_bit(num), expected)
        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        assert_equal(bits.flip_bit(num), expected)
        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        assert_equal(bits.flip_bit(num), expected)
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()

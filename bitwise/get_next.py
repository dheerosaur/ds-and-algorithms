from nose.tools import assert_equal, assert_raises


class Bits(object):

    def get_next_largest(self, num):
        if num is None or num <= 0:
            raise Exception
        num_zeros = 0
        num_ones = 0
        num_copy = num
        answer = num

        while num_copy & 1 == 0 and num_copy:
            num_zeros += 1
            num_copy >>= 1

        while num_copy & 1 == 1 and num_copy:
            num_ones += 1
            num_copy >>= 1

        index = num_zeros + num_ones
        # set the bit before index
        answer |= (1 << index)
        # clear all bits below index
        answer &= ~((1 << index) - 1)
        answer |= ((1 << (num_ones - 1)) - 1)
        return answer

    def get_next_smallest(self, num):
        if num is None or num <= 0:
            raise Exception
        num_zeros = 0
        num_ones = 0
        num_copy = num
        ans = num

        while num_copy & 1 == 1 and num_copy:
            num_ones += 1
            num_copy >>= 1

        while num_copy & 1 == 0 and num_copy:
            num_zeros += 1
            num_copy >>= 1

        index = num_ones + num_zeros
        ans &= ~(1 << index)
        ans &= ~((1 << index) - 1)
        ans |= ((1 << num_ones + 1) - 1)
        return ans


class TestBits(object):

    def test_get_next_largest(self):
        bits = Bits()
        assert_raises(Exception, bits.get_next_largest, None)
        assert_raises(Exception, bits.get_next_largest, 0)
        assert_raises(Exception, bits.get_next_largest, -1)
        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        assert_equal(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    def test_get_next_smallest(self):
        bits = Bits()
        assert_raises(Exception, bits.get_next_smallest, None)
        assert_raises(Exception, bits.get_next_smallest, 0)
        assert_raises(Exception, bits.get_next_smallest, -1)
        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        assert_equal(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')


def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


if __name__ == '__main__':
    main()

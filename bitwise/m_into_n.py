from nose.tools import assert_equal


def print_binary(n):
    print('{0:016b}'.format(n))


class Bits(object):

    def insert_m_into_n(self, m, n, i, j):
        # first set bits i to j = 0 in n
        mask = ~((1 << j) - 1) | ((1 << i) - 1)
        n_with_zeroes = n & mask
        # set all bits except last j to zero in m
        m_mask = (m & (1 << j + 1) - 1) << i
        return n_with_zeroes | m_mask


class TestBit(object):

    def test_insert_m_into_n(self):
        n = int('0000010000111101', base=2)
        m = int('0000000000010011', base=2)
        expected = int('0000010001001101', base=2)
        bits = Bits()
        assert_equal(bits.insert_m_into_n(m, n, i=2, j=6), expected)
        print('Success: test_insert_m_into_n')


def main():
    test = TestBit()
    test.test_insert_m_into_n()


if __name__ == '__main__':
    main()

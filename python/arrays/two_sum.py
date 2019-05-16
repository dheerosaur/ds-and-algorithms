from nose.tools import assert_equal


def two_sum_hmap(A, target):
    hmap = dict()
    for i, num in enumerate(A):
        if num in hmap:
            return (hmap[num], i)
        hmap[target - num] = i
    return None


class TestBit(object):

    def test_two_sum(self, two_sum_f):
        assert_equal(two_sum_f([1, 2, 3, 4, 5], 6), (1, 3))
        assert_equal(two_sum_f([1, 2, 3, 4, 5], 4), (0, 2))
        assert_equal(two_sum_f([-1, 2, 9, 0, 4], 3), (0, 4))
        assert_equal(two_sum_f([1, 2, 3, 4, 5], 0), None)
        print('Success: {}'.format(two_sum_f.__name__))


def main():
    test = TestBit()
    test.test_two_sum(two_sum_hmap)


if __name__ == '__main__':
    main()

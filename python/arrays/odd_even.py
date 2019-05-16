"""
"""
from nose.tools import assert_equal


def odd_even(A):
    """
    :type A: List[int]
    :rtype List[int]

    - in-place modification of the array
    - pointers from start and end
    """
    left, right = 0, len(A) - 1
    while left < right:
        if A[left] % 2 == 0:
            left += 1
        else:
            A[left], A[right] = A[right], A[left]
            right -= 1
    return A


class Test(object):

    def test_odd_even(self, odd_even_f):
        assert_equal(odd_even_f([1, 2, 3, 4]), [4, 2, 3, 1])
        assert_equal(odd_even_f([2, 2, 3, 3]), [2, 2, 3, 3])
        assert_equal(odd_even_f([]), [])
        assert_equal(odd_even_f([0]), [0])
        print('Success: {}'.format(odd_even_f.__name__))


def main():
    test = Test()
    test.test_odd_even(odd_even)


if __name__ == '__main__':
    main()

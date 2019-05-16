"""
Given a sorted array A of N elements, for each index i of the array,
find how many elements in the array lie between A[i] and 2 * A[i]
"""

from nose.tools import assert_equal
from bisect import bisect_left


def between_ai_2ai(A):
    """
    Brute-force algorithm O(n^2)
    """
    result = []
    for i in range(len(A)):
        count = 0
        for j in range(i + 1, len(A)):
            if A[j] >= 2 * A[i]:
                break
            count += 1
        result.append(count)

    return result


def between_ai_2ai_bs(A):
    """
    Using in-built binary search bisect_left in Python - O(n * log(n))
    We search for the position for 2*i and append difference - 1
    """
    result = []
    for i in range(len(A)):
        pos = bisect_left(A, 2 * A[i])
        result.append(pos - i - 1)
    return result


def between_ai_2ai_linear(A):
    """
    We will use two pointers and catch one up to other
    """
    result = []
    j = 0
    for i in range(len(A)):
        if i == j:
            while j < len(A) and A[j] < 2 * A[i]:
                j += 1
        result.append(j - i - 1)
    return result


class Test(object):

    def test_between_ai_2ai(self, between_ai_2ai_f):
        assert_equal(between_ai_2ai_f([1, 1, 2, 8, 10]),
                     [1, 0, 0, 1, 0])
        print('Success: {}'.format(between_ai_2ai_f.__name__))


def main():
    test = Test()
    test.test_between_ai_2ai(between_ai_2ai)
    test.test_between_ai_2ai(between_ai_2ai_bs)
    test.test_between_ai_2ai(between_ai_2ai_linear)


if __name__ == '__main__':
    main()

"""
Given a Binary Search Tree, find the sum of all leaf nodes.
"""
from nose.tools import assert_equal
from math import log2, floor


def sum_of_leaves_bst(tree):
    """
    If tree is represented as an array
    """
    length = len(tree)
    if length == 0:
        return 0
    height = floor(log2(length))
    return sum(tree[2 ** height - 1:])


class Test(object):

    def test_sum_of_leaves_bst(self, sum_of_leaves_bst_f):
        assert_equal(sum_of_leaves_bst_f([]), 0)
        assert_equal(sum_of_leaves_bst_f([50]), 50)
        assert_equal(sum_of_leaves_bst_f([2, 4]), 4)
        assert_equal(sum_of_leaves_bst_f([67, 32, 42, 12, 45, 78]), 135)


def main():
    test = Test()
    test.test_sum_of_leaves_bst(sum_of_leaves_bst)


if __name__ == '__main__':
    main()

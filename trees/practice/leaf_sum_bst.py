from nose.tools import assert_equal


class Node:
    data = 0
    left = None
    right = None


def createNewNode(value):
    temp = Node()
    temp.data = value
    temp.left = None
    temp.right = None
    return temp


def newNode(root, data):
    if (root is None):
        root = createNewNode(data)
    elif (data < root.data):
        root.left = newNode(root.left, data)
    else:
        root.right = newNode(root.right, data)
    return root


def sum_of_leaves(root):
    if root is None:
        return 0
    if not (root.left or root.right):
        return root.data
    return sum_of_leaves(root.left) + sum_of_leaves(root.right)


def nth(root, n):
    pass


def main():
    def create_tree(case):
        root = None
        values = [int(x) for x in case.split()]
        for val in values:
            root = newNode(root, val)
        return root

    assert_equal(sum_of_leaves(create_tree("")), 0)
    assert_equal(sum_of_leaves(create_tree("45")), 45)
    assert_equal(sum_of_leaves(create_tree("67 34 82 12 45 78")), 135)
    assert_equal(nth(create_tree("67 34 82"), 0), 67)
    assert_equal(nth(create_tree("67 34 82"), 1), 34)
    assert_equal(nth(create_tree("67 34 82"), 2), 82)


if __name__ == "__main__":
    main()

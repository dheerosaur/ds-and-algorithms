"""
From Wikipedia

https://en.wikipedia.org/wiki/Tree_traversal

Practice before implementing in the Tree classes
"""

from linked_binary_tree import LinkedBinaryTree


def print_el(p):
    print(p.element(), end='')


def create_tree():
    t = LinkedBinaryTree()
    f = t._add_root('f')

    # left tree
    b = t._add_left(f, 'b')
    t._add_left(b, 'a')
    d = t._add_right(b, 'd')
    t._add_left(d, 'c')
    t._add_right(d, 'e')

    # right tree
    g = t._add_right(f, 'g')
    i = t._add_right(g, 'i')
    t._add_left(i, 'h')
    return t


def pre_order(tree, p):
    if p is None:
        return
    print_el(p)
    pre_order(tree, tree.left(p))
    pre_order(tree, tree.right(p))


def pre_order_iter(tree):
    if tree.is_empty():
        return ''
    s = [tree.root()]
    while s:
        p = s.pop()
        print_el(p)
        if tree.right(p):
            s.append(tree.right(p))
        if tree.left(p):
            s.append(tree.left(p))


def pre_order_ri(tree, p):
    yield p
    for c in tree.children(p):
        for other in pre_order_ri(tree, c):
            yield other


def post_order(tree, p):
    if p is None:
        return
    post_order(tree, tree.left(p))
    post_order(tree, tree.right(p))
    print_el(p)


def post_order_iter(tree):
    s, p = [], tree.root()
    last_visited = None
    while s or p is not None:
        if p is not None:
            s.append(p)
            p = tree.left(p)
        else:
            peek = s[-1]
            right = tree.right(peek)
            if right and last_visited != right:
                p = right
            else:
                print_el(peek)
                last_visited = s.pop()


def post_order_ri(tree, p):
    for c in tree.children(p):
        for other in post_order_ri(tree, c):
            yield other
    yield p


def in_order(tree, p):
    if p is None:
        return
    in_order(tree, tree.left(p))
    print_el(p)
    in_order(tree, tree.right(p))


def in_order_iter(tree):
    s, p = [], tree.root()
    while s or p is not None:
        if p is not None:
            s.append(p)
            p = tree.left(p)
        else:
            p = s.pop()
            print_el(p)
            p = tree.right(p)


def in_order_ri(tree, p):
    left = tree.left(p)
    right = tree.right(p)
    if left:
        for c in in_order_ri(tree, left):
            yield c
    yield p
    if right:
        for c in in_order_ri(tree, right):
            yield c


if __name__ == '__main__':
    t1 = create_tree()  # Binary tree

    pre_order_iter(t1)
    print()
    pre_order(t1, t1.root())
    print()
    for p in pre_order_ri(t1, t1.root()):
        print_el(p)
    print()
    for p in t1.preorder():
        print_el(p)
    print('\n')

    post_order_iter(t1)
    print()
    post_order(t1, t1.root())
    print()
    for p in post_order_ri(t1, t1.root()):
        print_el(p)
    print()
    for p in t1.postorder():
        print_el(p)
    print('\n')

    in_order_iter(t1)
    print()
    in_order(t1, t1.root())
    print()
    for p in in_order_ri(t1, t1.root()):
        print_el(p)
    print()
    for p in t1.inorder():
        print_el(p)
    print('\n')

    for p in t1.breadthfirst():
        print_el(p)

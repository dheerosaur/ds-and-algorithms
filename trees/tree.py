"""
Abstract base class Tree
"""


class Tree:
    """
    Abstract base class representing a tree structure
    """

    # -- Nested position class --
    class Position:
        """ An abstraction representing the location of a single element"""

        def element(self):
            "Return the element stored at this Position"
            raise NotImplementedError()

        def __eq__(self, other):
            "Return True if other Position represents the same location"
            raise NotImplementedError()

        def __ne__(self, other):
            "Return True if other does not represent the same location"
            return not (self == other)

    # -- Abstract methods to be implemented by subclasses --
    def root(self):
        "Return Position representing the tree's root"
        raise NotImplementedError()

    def parent(self, p):
        "Return Position representing p's parent"
        raise NotImplementedError()

    def num_children(self, p):
        "Return the number of children the Position p has"
        raise NotImplementedError()

    def children(self, p):
        "Generate an iteration of Positions representing p's children"
        raise NotImplementedError()

    def __len__(self):
        "Return total number of elements in the tree"
        raise NotImplementedError()

    # -- Concrete methods implemented in the class --
    def __iter__(self):
        "Generate an iteration of the tree's elements"
        for p in self.positions():
            yield p.element()

    def is_root(self, p):
        "Return True if Position p represents the root of the tree"
        return self.root() == p

    def is_leaf(self, p):
        "Return True if Position p doesn't have any children"
        return self.num_children(p) == 0

    def is_empty(self):
        "Return True if the tree is empty"
        return len(self) == 0

    def depth(self, p):
        "Return the number of levels separating Position p from the root"
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height(self, p):
        "Private method for calculating height of a Position p"
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        "Return the height of a Position p"
        if p is None:
            p = self.root()
        return self._height(p)


class BinaryTree(Tree):
    """
    Class representing a Binary tree structure
    """

    # -- Abstract methods to be implemented by subclasses --
    def left(self, p):
        """
        Return a Position representing p's left child

        Return None if p does not have a left child
        """
        raise NotImplementedError()

    def right(self, p):
        """
        Return a Position representing p's right child

        Return None if p does not have a right child
        """
        raise NotImplementedError()

    # -- Concrete methods implemented in the class --
    def sibling(self, p):
        """
        Return a Position representing p's sibling

        Return None if no sibling
        """
        parent = self.parent(p)
        if parent is None:                  # p must be the root
            return None                     # root has no sibling
        elif self.left(parent) == p:
            return self.right(parent)       # possibly None
        else:
            return self.left(parent)        # possibly None

    def children(self, p):
        "Generate an iteration of Positions representing p's children"
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

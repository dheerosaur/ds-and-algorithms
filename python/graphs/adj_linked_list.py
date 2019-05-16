"""
Implementation of Graph using Adjacency list

List here means linked list
"""


class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class Graph:

    def __init__(self, size):
        self.size = size
        self.graph = [None] * size

    def add_edge(self, x, y):
        # prepend x node to y adjlist
        src = Node(x)
        src.next = self.graph[y]
        self.graph[y] = src

        # prepend y node to x adjlist
        dst = Node(y)
        dst.next = self.graph[x]
        self.graph[x] = dst

    def print_graph(self):
        for i in range(self.size):
            node = self.graph[i]
            print('At {}'.format(i), end=' ')
            while node:
                print(' -> {}'.format(node.val), end=' ')
                node = node.next
            print()


def test():
    G = Graph(6)
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(0, 4)
    G.print_graph()


if __name__ == '__main__':
    test()

from collections import defaultdict


class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.pre = None
        self.post = None
        self.status = 'new'

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return str(self.value)


def construct_graph(nv, edges, directed):
    vertices = {i: Node(i) for i in range(nv)}
    g = defaultdict(list)
    for edge in edges:
        u, v = [vertices[int(x)] for x in edge.split()]
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g


def get_graph_from_file(fname, directed=False):
    with open(fname) as f:
        nv = int(f.readline())
        edgelist = f.read().strip().split('\n')[1:]
        return construct_graph(nv, edgelist, directed)


def orders(g):
    clock = 0
    visited = set()

    def dfs(v, clock):
        visited.add(v)
        clock += 1
        v.pre = clock
        for w in g[v]:
            if w not in visited:
                w.parent = v
                clock = dfs(w, clock)
        clock += 1
        v.post = clock
        return clock

    for v in g:
        if v not in visited:
            clock = dfs(v, clock)


def orders_fun(g):
    clock = [0]
    visited = set()

    def dfs(v):
        visited.add(v)
        previsit(v)
        for w in g[v]:
            if w not in visited:
                w.parent = v
                dfs(w)
        postvisit(v)

    def preprocess():
        clock[0] = 0

    def previsit(v):
        clock[0] += 1
        v.pre = clock[0]

    def postvisit(v):
        clock[0] += 1
        v.post = clock[0]

    preprocess()
    for v in g:
        if v not in visited:
            dfs(v)


def is_acyclic(g):
    def dfs_acylcic(v):
        v.status = 'act'
        for w in g[v]:
            if w.status == 'act':
                return False
            elif w.status == 'new':
                if not dfs_acylcic(w):
                    return False
        v.status = 'fin'
        return True

    keys = list(g.keys())
    for v in keys:
        if v.status == 'new':
            if not dfs_acylcic(v):
                return False
    return True


def top_sort(g):
    keys = list(g.keys())
    S = []

    def top_sort_dfs(v):
        v.status = 'active'
        for w in g[v]:
            if w.status == 'new':
                top_sort_dfs(w)
            elif w.status == 'active':
                raise Exception('not cyclic')
        v.status = 'finished'
        S.append(v)

    for v in keys:
        if v.status == 'new':
            top_sort_dfs(v)
    return S


def top_sort_simple(g):
    visited = set()
    result = []

    def dfs(v):
        visited.add(v)
        for w in g[v]:
            if w not in visited:
                dfs(v)
        result.append(v)

    for v in g:
        if v not in visited:
            dfs(v)
    return result


if __name__ == '__main__':
    # g = get_graph_from_file('../data/tinyG.txt')
    # orders_fun(g)

    # dg1 = get_graph_from_file('../data/tinyDG.txt', directed=True)
    # print(is_acyclic(dg1))

    # dg2 = get_graph_from_file('../data/tinyDAG.txt', directed=True)
    # print(is_acyclic(dg2))

    dag = get_graph_from_file('../data/tinyDAG.txt', directed=True)
    print(top_sort(dag))

    dag = {0: [], 1: [0], 2: [0], 3: [1, 2], 4: [3]}
    print(top_sort_simple(dag))

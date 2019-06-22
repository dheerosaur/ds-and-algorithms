from collections import deque
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.reset()

    def reset(self):
        self.processed = set()
        self.discovered = set()
        self.parents = dict()

    def nvertices(self):
        return len(self.graph)

    def vertices(self):
        return self.graph.keys()

    def edges(self):
        return [(u, v)
                for u in self.graph
                for v in self.graph[u]]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, s=None):
        "Breadth first search starting at s"
        if s is None:
            s = next(iter(self.graph))
        visited = [0] * len(self.graph)
        queue = deque([s])
        visited[s] = 1

        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for adj in self.graph[v]:
                if not visited[adj]:
                    queue.append(adj)
                    visited[adj] = 1

    def dfs(self):
        visited = [0] * len(self.graph)

        def helper(s):
            visited[s] = 1
            print(s, end=' ')
            for v in self.graph[s]:
                if not visited[v]:
                    helper(v)

        for s in self.graph:
            if not visited[s]:
                helper(s)

    def bfs_full(self, s, p):
        """S is the start verted
        p is the processor"""
        q = deque([s])
        self.discovered.add(s)

        while q:
            u = q.popleft()
            p.process_vertex_early(u)
            self.processed.add(u)
            for v in self.graph[u]:
                if v not in self.processed:
                    p.process_edge(u, v)
                if v not in self.discovered:
                    q.append(v)
                    self.discovered.add(v)
                    self.parents[v] = u
            p.process_vertex_late(u)


class Processor:
    def process_vertex_early(self, u):
        pass

    def process_edge(self, u, v):
        pass

    def process_vertex_late(self, u):
        pass


class CCProcessor(Processor):
    def process_vertex_early(self, u):
        print(u, end=' ')


class TwoColorProcessor(Processor):
    def __init__(self, g):
        self.bipartite = True
        self.colors = {u: 0 for u in g.vertices()}

    def process_edge(self, u, v):
        if self.colors[u] != self.colors[v]:
            self.bipartite = False
        self.colors[v] = 2 if self.colors[u] == 1 else 1


def construct_graph(edges):
    g = Graph()
    for edge in edges:
        u, v = [int(x) for x in edge.split()]
        g.add_edge(u, v)
    return g


def find_path(start, end, parents):
    if start == end or end not in parents:
        print(start, end=' ')
    else:
        find_path(start, parents[end], parents)
        print(end, end=' ')


def connected_components(g):
    cnum = 0
    p = CCProcessor()

    for u in g.vertices():
        if u not in g.discovered:
            cnum += 1
            print('Component', cnum)
            g.bfs_full(u, p)
            print()
    return cnum


def two_color(g):
    p = TwoColorProcessor(g)

    for u in g.vertices():
        if u not in g.discovered:
            p.colors[u] = 1
            g.bfs_full(u, p)
    return p.bipartite


def get_graph_from_file(fname):
    with open(fname) as f:
        edgelist = f.read().strip().split('\n')[2:]
        return construct_graph(edgelist)


if __name__ == '__main__':
    # Application 1: Find path
    # g = get_graph_from_file('../data/tinyCG.txt')
    # g.bfs_full(0, Processor())
    # find_path(0, 4, g.parents)

    # Application 2: Connected components
    #  g = get_graph_from_file('../data/tinyG.txt')
    #  n = connected_components(g)
    #  print(f'Graph has {n} connected components')

    # Application 3: Two coloring
    g = get_graph_from_file('../data/tinyG.txt')
    print('Bipartite' if two_color(g) else 'Non-bipartite')

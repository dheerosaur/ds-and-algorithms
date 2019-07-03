from collections import defaultdict


def construct_graph(edges):
    g = defaultdict(list)
    for edge in edges:
        u, v = [int(x) for x in edge.split()]
        g[u].append(v)
        g[v].append(u)
    return g


def get_graph_from_file(fname):
    with open(fname) as f:
        edgelist = f.read().strip().split('\n')[2:]
        return construct_graph(edgelist)



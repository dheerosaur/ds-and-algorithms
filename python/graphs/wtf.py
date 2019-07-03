from collections import deque
from base import get_graph_from_file


def dfs(g):
    result = []
    visited = set()

    def helper(u):
        if u not in visited:
            visited.add(u)
            result.append(u)
            for v in g[u]:
                helper(v)

    helper(next(iter(g)))
    return result


def dfs_iter(g):
    result = []
    visited = set()

    def helper(u):
        stack = [u]
        while stack:
            v = stack.pop()
            if v not in visited:
                result.append(v)
                visited.add(v)
                for w in g[v]:
                    stack.append(w)

    helper(next(iter(g)))
    return result


def bfs(g, start):
    visited = set()
    result = []

    q = deque([start])
    while q:
        v = q.popleft()
        if v not in visited:
            visited.add(v)
            result.append(v)
            for w in g[v]:
                q.append(w)
    return result


def find_path(g, src, dst):
    def get_parents_using_bfs(g, start):
        visited = set()
        parents = {}
        q = deque([(-1, start)])
        while q:
            p, v = q.popleft()
            if v not in visited:
                visited.add(v)
                parents[v] = p
                for w in g[v]:
                    q.append((v, w))
        return parents

    parents = get_parents_using_bfs(g, src)

    def helper(src, dst):
        if src == -1:
            return
        else:
            helper(parents[src], dst)
            print(src, end=' ')

    helper(dst, src)


def bfs_all(g):
    visited = set()
    count = 1
    result = []

    for v in g:
        if v not in visited:
            comp = bfs(g, v)
            visited.update(comp)
            result.append((count, comp))
            count += 1
    return result


if __name__ == '__main__':
    # DFS
    #  g = get_graph_from_file('../data/tinyCG.txt')
    #  print('DFS recursive', dfs(g))

    #  g = get_graph_from_file('../data/tinyCG.txt')
    #  print('DFS iterative', dfs_iter(g))

    #  g = get_graph_from_file('../data/tinyCG.txt')
    #  print('Breadth first search', bfs(g, 0))

    #  g = get_graph_from_file('../data/tinyG.txt')
    #  print('Components', bfs_all(g))

    g = get_graph_from_file('../data/tinyCG.txt')
    find_path(g, 1, 4)

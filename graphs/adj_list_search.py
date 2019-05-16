from collections import deque
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, s):
        "Breadth first search starting at s"
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


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.bfs(1)
    print()
    g.dfs()
    print()


if __name__ == '__main__':
    main()

G = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'F'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
}


def find_paths(g, start, end):
    def find_path(g, start, end, path):
        path = path + [start]
        if start == end:
            return path
        if end not in g:
            return None
        for node in g[start]:
            if node not in path:
                np = find_path(g, node, end, path)
                explorations.append(np)
        return None

    explorations = []
    find_path(g, start, end, [])
    return [path for path in explorations if path]


print(find_paths(G, 'A', 'F'))

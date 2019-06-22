# Read graph file and create an adjacency matrix
# for an undirected graph and directed one


def main(lines, directed=False):
    nv = int(lines[0])
    matrix = [[0 for _ in range(nv)] for _ in range(nv)]
    for line in lines[2:]:
        src, dst = [int(x) for x in line.split()]
        matrix[src][dst] = 1
        if not directed:
            matrix[dst][src] = 1
    return matrix


if __name__ == '__main__':
    with open('../data/tinyCG.txt') as f:
        flines = f.read().strip().splitlines()
        print(main(flines, directed=False))
        print(main(flines, directed=True))

def min_swaps(arr):
    pos = sorted(enumerate(arr), key=lambda x: x[1])
    g = {x: pos[x][0] for x in range(len(pos))}
    visited = {k: 0 for k in g}

    swaps = 0
    for k in g:
        nodes = 0
        j = k
        while not visited[j]:
            visited[j] = 1
            j = g[j]
            nodes += 1
        if nodes:
            swaps += nodes - 1
    return swaps


def main():
    cases = [
        # [1, 2, 5, 3, 4],
        [1, 40, 90, 200, 2, 6],
    ]
    for case in cases:
        print(min_swaps(case))


if __name__ == '__main__':
    main()

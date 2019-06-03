from time import time


def compute_average(n):
    # Demonstratesamortized runtime of O(1) for append
    data = []
    start = time()
    for _ in range(n):
        data.append(None)
    elapsed = time() - start
    return round(elapsed * 1e6, 2)


def main():
    for n in range(3, 8):
        size = 10 ** n
        print(size, compute_average(size))


if __name__ == '__main__':
    main()

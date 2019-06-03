#!/usr/bin/env python3
import sys
from collections import Counter


def countTriplets(A, nn):
    count, singles, pairs = 0, Counter(), Counter()
    for item in reversed(A):
        last = item * nn
        if last in pairs:
            count += pairs[last]
        if last in singles:
            pairs[item] += singles[last]
        singles[item] += 1
    return count


if __name__ == '__main__':
    fptr = sys.stdout

    with open('data/triplets1.txt') as f:
        nr = f.readline().rstrip().split()

        n = int(nr[0])

        r = int(nr[1])

        arr = list(map(int, f.readline().rstrip().split()))

        ans = countTriplets(arr, r)

        fptr.write(str(ans) + '\n')

        fptr.close()

#!/bin/python3

import sys
import collections


def freqQuery(queries):
    result = []
    freqs = collections.Counter()
    counter = collections.Counter()
    for q, val in queries:
        if q == 1:
            freqs[counter[val]] -= 1
            counter[val] += 1
            freqs[counter[val]] += 1
        elif q == 2 and counter[val]:
            freqs[counter[val]] -= 1
            counter[val] -= 1
            freqs[counter[val]] += 1
        elif q == 3:
            result.append(1 if freqs[val] else 0)
    return result


def main(fname):
    print(fname)
    fptr = sys.stdout

    with open(fname) as f:
        q = int(f.readline().strip())

        queries = []

        for _ in range(q):
            query = list(map(int, f.readline().rstrip().split()))
            queries.append(query)

        ans = freqQuery(queries)

        fptr.write('\n'.join(map(str, ans)))
        fptr.write('\n')


if __name__ == '__main__':
    main('data/freq_query1.txt')
    main('data/freq_query2.txt')
    main('data/freq_query3.txt')

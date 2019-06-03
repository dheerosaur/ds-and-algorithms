import heapq
import random
import collections


class MinHeap:
    def __init__(self, arr):
        self.A = arr.copy()
        heapq.heapify(self.A)

    def __len__(self):
        return len(self.A)

    def replace(self, n):
        return heapq.heapreplace(self.A, n)

    def push(self, n):
        heapq.heappush(self.A, n)

    def pop(self):
        return heapq.heappop(self.A)

    def get_min(self):
        return heapq.nsmallest(1, self.A)[0]


class MaxHeap:
    def __init__(self, arr):
        self.A = [-x for x in arr]
        heapq.heapify(self.A)

    def __len__(self):
        return len(self.A)

    def replace(self, n):
        return -heapq.heapreplace(self.A, -n)

    def push(self, n):
        heapq.heappush(self.A, -n)

    def pop(self):
        return -heapq.heappop(self.A)

    def get_max(self):
        return -heapq.nsmallest(1, self.A)[0]


class NumStream:
    def __init__(self):
        self.left = MaxHeap([float('-inf')])
        self.right = MinHeap([float('inf')])

    def push(self, num):
        ln, rn = len(self.left), len(self.right)
        lmax, rmin = self.left.get_max(), self.right.get_min()
        if ln < rn:
            if num < rmin:
                self.left.push(num)
            else:
                self.left.push(self.right.replace(num))
        elif rn < ln:
            if num > lmax:
                self.right.push(num)
            else:
                self.right.push(self.left.replace(num))
        else:
            if num < rmin:
                self.left.push(num)
            else:
                self.right.push(num)

    def get_median(self):
        ln, rn = len(self.left), len(self.right)
        if ln == rn:
            med = (self.left.get_max() + self.right.get_min()) / 2
        elif ln < rn:
            med = self.right.get_min()
        else:
            med = self.left.get_max()
        return med

    def add_and_get_median(self, num):
        self.push(num)
        return self.get_median()


def median_array(values):
    arr, n = sorted(values), len(values)
    if n % 2:
        return arr[n // 2]
    return (arr[n // 2 - 1] + arr[n // 2]) / 2


class MedianUsingCounter:
    def __init__(self):
        self.size = 0
        self.ctr = collections.Counter([])

    def push(self, num):
        self.ctr[num] += 1
        self.size += 1

    def get_median(self):
        if self.size % 2:
            i1, i2 = self.size // 2, self.size // 2
        else:
            i1, i2 = self.size // 2 - 1, self.size // 2
        k = 0
        counts = iter(sorted(self.ctr.items()))
        while k <= i1:
            m1, count = next(counts)
            k += count

        k = 0
        counts = iter(sorted(self.ctr.items()))
        while k <= i2:
            m2, count = next(counts)
            k += count

        return (m1 + m2) / 2

    def add_and_get_median(self, num):
        self.push(num)
        return self.get_median()


def main():
    s = NumStream()
    mc = MedianUsingCounter()
    values = []
    for _ in range(100):
        num = random.randrange(0, 100)
        values.append(num)
        med1 = median_array(values)
        med2 = s.add_and_get_median(num)
        med3 = mc.add_and_get_median(num)
        assert med1 == med2 == med3


if __name__ == '__main__':
    main()

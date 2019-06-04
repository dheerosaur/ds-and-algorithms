import random
import bisect


def median(values):
    arr, n = sorted(values), len(values)
    return (
        arr[n // 2] if n % 2 else
        (arr[n // 2] + arr[n // 2 - 1]) / 2
    )


def replace(arr, i, j):
    pos = bisect.bisect_left(arr, i)
    arr[pos] = j
    arr.sort()


def activityNotifications_bf(expenditure, d):
    # sliding window
    n = len(expenditure)
    count = 0
    window = sorted(expenditure[:d])
    for i in range(d, n):
        mdn = median(window)
        if expenditure[i] >= (mdn * 2):
            count += 1
        replace(window, expenditure[i - d], expenditure[i])
    return count


class MedianUsingCounter:
    def __init__(self, arr):
        self.ctr = [0 for _ in range(201)]
        self.size = len(arr)
        for item in arr:
            self.ctr[item] += 1

    def replace(self, rem, add):
        self.ctr[rem] -= 1
        self.ctr[add] += 1

    def get_median(self):
        return (
            self.get_median_for_odd() if self.size % 2 else
            self.get_median_for_even()
        )

    def _at(self, pos):
        j, k, ret = 0, 0, None
        while k <= pos:
            k += self.ctr[j]
            ret = j
            j += 1
        return ret

    def get_median_for_odd(self):
        return self._at(self.size // 2)

    def get_median_for_even(self):
        return (
            self._at(self.size // 2) +
            self._at(self.size // 2 - 1)
        ) / 2


def activityNotifications(expenditure, d):
    m = MedianUsingCounter(expenditure[:d])
    count = 0
    for i in range(d, len(expenditure)):
        cur = expenditure[i]
        med = m.get_median()
        if cur >= (2 * med):
            count += 1
        m.replace(expenditure[i-d], cur)
    return count


if __name__ == '__main__':
    cases = [
        ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5),
        ([1, 2, 3, 4, 4], 4),
    ]

    for k in range(100, 10000, 100):
        expenditure = [random.randrange(0, 10) for _ in range(k)]
        cases.append((expenditure, random.randrange(3, 10)))

    for case in cases:
        fa = activityNotifications(*case)
        bf = activityNotifications_bf(*case)
        assert bf == fa

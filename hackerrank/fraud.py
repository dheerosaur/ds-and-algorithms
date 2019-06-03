import random
import bisect


def median(values):
    arr, n = sorted(values), len(values)
    if n % 2:
        return arr[n // 2]
    else:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2


def replace(arr, i, j):
    pos = bisect.bisect_left(arr, i)
    arr[pos] = j
    arr.sort()


def activityNotifications(expenditure, d):
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


if __name__ == '__main__':
    for k in range(100, 10000, 100):
        case = [random.randrange(1, 10) for _ in range(k)]
        print(activityNotifications(case, random.randrange(3, 10)))

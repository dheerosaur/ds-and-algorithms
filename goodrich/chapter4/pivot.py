def pivot(seq, k):
    def helper(left, right):
        if left > right:
            return
        if seq[left] < k:
            helper(left + 1, right)
        elif seq[right] > k:
            helper(left, right - 1)
        else:
            seq[left], seq[right] = seq[right], seq[left]
            helper(left + 1, right - 1)

    helper(0, len(seq) - 1)
    return seq


print(pivot([9, 6, 2, 5, 4, 3], 4))
print(pivot([9, 7, 8, 6, 2, 4, 3], 5))

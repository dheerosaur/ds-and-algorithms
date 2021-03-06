def even_odd(seq):
    def helper(left, right):
        if left > right:
            return
        if seq[left] % 2 == 0:
            helper(left + 1, right)
        elif seq[right] % 2 == 1:
            helper(left, right - 1)
        else:
            seq[left], seq[right] = seq[right], seq[left]
            helper(left + 1, right - 1)

    helper(0, len(seq) - 1)
    return seq


print(even_odd(list(range(10))))
print(even_odd([9, 1, 2, 3, 6]))

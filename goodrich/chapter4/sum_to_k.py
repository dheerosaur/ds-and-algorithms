def sum_to_k(seq, k):
    def helper(left, right):
        if left > right:
            return False
        return (
            helper(left + 1, right) or
            helper(left, right - 1) or
            (seq[left] + seq[right] == k)
        )
    return helper(0, len(seq) - 1)


print(sum_to_k(list(range(10)), 9))
print(sum_to_k([1, 3, 5, 7], 9))

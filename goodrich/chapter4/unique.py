def unique(seq, target, count=0):
    if not seq:
        return count == 1
    if seq[0] == target:
        count += 1
    return unique(seq[1:], target, count)


print(unique(range(10), 5))
print(unique([1, 2, 1, 3], 1))

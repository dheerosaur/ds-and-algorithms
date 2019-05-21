def log2(num, n=0):
    if num == 1:
        return n
    return log2(num // 2, n + 1)


print(log2(10))
print(log2(1024))

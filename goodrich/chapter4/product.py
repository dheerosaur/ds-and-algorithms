def mul(x, y):
    if x == 0:
        return 0
    return y + mul(x - 1, y)


print(mul(10, 20))
print(mul(99, 98))

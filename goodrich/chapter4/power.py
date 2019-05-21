def power(x, n):
    if n == 0:
        return 1
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x
    return result


print(power(2, 10))
print(power(3, 4))

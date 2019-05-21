
def max_element(sequence, ans=0):
    if not sequence:
        return ans
    ans = max(ans, sequence[0])
    return max_element(sequence[1:], ans)


print(max_element([]))
print(max_element([1]))
print(max_element(range(20)))

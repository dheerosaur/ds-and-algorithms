def is_palindrome(word):
    def helper(s, start, end):
        if start >= end:
            return True
        return (
            s[start] == s[end] and
            helper(s, start + 1, end - 1)
        )
    return helper(word, 0, len(word) - 1)


print(is_palindrome('racecar'))
print(is_palindrome('message'))
print(is_palindrome('gohangasalamiimalasagnahog'))

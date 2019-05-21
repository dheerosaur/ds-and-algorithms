def has_more_vowels(word):
    def helper(s, vow, cons):
        if not s:
            return vow > cons
        if s[0] in 'aeiou':
            vow += 1
        else:
            cons += 1
        return helper(s[1:], vow, cons)

    return helper(word, 0, 0)


print(has_more_vowels('alabama'))
print(has_more_vowels('iota'))
print(has_more_vowels('crank'))

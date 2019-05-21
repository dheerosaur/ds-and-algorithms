

def rev_seq(seq):
    def helper(s, left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(s, left + 1, right - 1)

    helper(seq, 0, len(seq) - 1)


ll = list(range(10))
rev_seq(ll)
print(ll)

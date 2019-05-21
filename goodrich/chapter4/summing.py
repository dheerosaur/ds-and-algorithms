

def sumem(seq):
    if not seq:
        return 0
    return seq[0] + sumem(seq[1:])


print(sumem([]))
print(sumem(range(2)))
print(sumem(range(10)))

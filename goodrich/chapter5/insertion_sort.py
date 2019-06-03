

def sel_sort(A):
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
    return A


def insertion_sort(A):
    for i in range(1, len(A)):
        cur = A[i]
        j = i
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur


def main():
    A = [1, 2, 5, 3, 9, 4]
    insertion_sort(A)
    print(A)


if __name__ == '__main__':
    main()

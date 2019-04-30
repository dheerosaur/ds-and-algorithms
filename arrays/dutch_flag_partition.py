"""
Write a program that takes an array A and index i into A, and
rearranges the elements such that all elements less than A[i] (the pivot)
appear first, followed by elements equal to the pivot, followed by
elements greater than the pivot

"""


def dutch_flag_partition(A, pivot_index):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition_2(A, pivot_index):
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


def dutch_flag_partition_3(A, pivot_index):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


class Test(object):

    def assert_dutch(self, A, pivot):
        i = 0
        # Traverse the smaller section
        while i < len(A) and A[i] < pivot:
            i += 1
        while i < len(A) and A[i] == pivot:
            i += 1
        while i < len(A) and A[i] > pivot:
            i += 1
        assert(i == len(A))

    def test_dutch(self, dutch_fun, A, pivot_index):
        pivot = A[pivot_index]
        dutch_fun(A, pivot_index)
        self.assert_dutch(A, pivot)

    def test_dutch_flag_partition(self, f):
        self.test_dutch(f, [1, 2, 3, 4], 2)
        self.test_dutch(f, [4, 8, 2, 3, 9, 6], 3)
        print('Success: {}'.format(f.__name__))


def main():
    test = Test()
    test.test_dutch_flag_partition(dutch_flag_partition)
    test.test_dutch_flag_partition(dutch_flag_partition_2)
    test.test_dutch_flag_partition(dutch_flag_partition_3)


if __name__ == '__main__':
    main()

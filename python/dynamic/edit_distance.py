

class Solution:

    def calc_edits(self, M, A: str, B: str) -> None:
        i, j = len(M) - 1, len(M[0]) - 1
        changes = []
        while not (i == 0 or j == 0):
            if A[i-1] == B[j-1]:
                i, j = i - 1, j - 1
            elif M[i][j] == M[i - 1][j - 1] + 1:
                changes.append(f'Edit {A[i - 1]} to {B[j - 1]}')
                i, j = i - 1, j - 1
            elif M[i][j] == M[i][j - 1] + 1:
                changes.append(f'Insert {B[i]}')
                j = j - 1
            elif M[i][j] == M[i-1][j] + 1:
                changes.append(f'Insert {A[j]}')
                i = i - 1
        return changes[::-1]

    def editDistance(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        M = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        M[0] = list(range(n + 1))
        for i in range(m + 1):
            M[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                insertion = M[i][j - 1] + 1
                deletion = M[i - 1][j] + 1
                mismatch = M[i - 1][j - 1] + 1
                match = M[i - 1][j - 1]

                if A[i - 1] == B[j - 1]:
                    M[i][j] = min(insertion, deletion, match)
                else:
                    M[i][j] = min(insertion, deletion, mismatch)
        print(self.calc_edits(M, A, B))
        return f'{M[-1][-1]} edits'


def test():
    sol = Solution()
    cases = [
        ('EDITING', 'DISTANCE'),
    ]
    for case in cases:
        print(sol.editDistance(*case))


if __name__ == '__main__':
    test()

from typing import List


class Solution:

    def construct_lcs(self, M: List[List[int]], A: str, B: str) -> str:
        longest, ret = M[-1][-1], []
        m, n = len(M[0]) - 1, len(M) - 1
        for i in range(m, 0, -1):
            if longest == 0:
                break
            for j in range(n, 0, -1):
                if A[i - 1] == B[j - 1] and M[j][i] == longest:
                    ret.append(A[i - 1])
                    longest = longest - 1
        return ''.join(reversed(ret))

    def longest_common_subseq(self, A: str, B: str) -> int:
        m, n = len(A) + 1, len(B) + 1
        M = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                if A[j - 1] == B[i - 1]:
                    nmax = M[i-1][j - 1] + 1
                else:
                    nmax = max(M[i-1][j], M[i][j-1])
                M[i][j] = nmax
        return M[-1][-1], self.construct_lcs(M, A, B)


def test():
    sol = Solution()
    cases = [
        ('EDITING', 'DISTANCE'),
        ('TESTING', 'VESTING'),
        ('ABC', 'ABCDEABCD'),
        ('ABDEABCD', 'ABCD'),
        ('thou shalt not', 'you should not'),
    ]
    for case in cases:
        print(sol.longest_common_subseq(*case))


if __name__ == '__main__':
    test()

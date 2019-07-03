from typing import List


class Solution:
    def knapsack_no_rep(self, vw: List[List[int]], W: int) -> int:
        n = len(vw)
        M = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                v, w = vw[i - 1]
                if j >= w:
                    exc = M[i - 1][j]
                    inc = M[i - 1][j - w] + v
                    M[i][j] = max(inc, exc)
        max_val = M[-1][-1]

        # compute chosen
        k, chosen = W, [0] * n
        for i in range(n, 0, -1):
            v, w = vw[i - 1]
            inc = M[i - 1][k - w] + v
            if M[i][k] == inc:
                chosen[i - 1] = 1
                k = k - w

        return max_val, [x[0] for x, c in zip(vw, chosen) if c]

    def knapsack_rep(self, vw: List[List[int]], W: int) -> int:
        vals, weights = {}, {v: w for v, w in vw}
        dp = [0 for _ in range(W + 1)]
        for i in range(1, W + 1):
            for v, w in vw:
                total = v + dp[i - w]
                if w <= i and total > dp[i]:
                    dp[i] = total
                    vals[total] = v
        max_val = dp[-1]

        # compute chosen
        k, chosen = max_val, []
        while k > 0:
            chosen.append((vals[k], weights[vals[k]]))
            k = k - vals[k]
        return max_val, chosen[::-1]


def test():
    sol = Solution()
    cases = [
        ([[30, 6], [14, 3], [16, 4], [9, 2]], 10)
    ]
    for case in cases:
        print(sol.knapsack_rep(*case))
        print(sol.knapsack_no_rep(*case))


if __name__ == '__main__':
    test()

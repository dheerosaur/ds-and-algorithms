
class Solution:

    def climb_iter(self, N):
        res = [1, 1, 2]
        if N < 3:
            return res[N]

        for _ in range(N - 2):
            res[0], res[1], res[2] = \
                res[1], res[2], sum(res)
        return res[-1]

    def climb_recur(self, N):
        """
        Number of ways to climb n stairs with steps of magintude 1, 2, 3
        """
        def f(n, level=0):
            if n in [1, 2, 3]:
                return [1, 2, 4][n - 1]
            return (
                f(n - 1, level + 1) +
                f(n - 2, level + 1) +
                f(n - 3, level + 1)
            )
        return f(N)


def test():
    sol = Solution()
    cases = [
        5, 20
    ]
    for case in cases:
        print(sol.climb_recur(case))
        print(sol.climb_iter(case))


if __name__ == '__main__':
    test()

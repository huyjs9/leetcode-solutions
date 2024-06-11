# Level: Medium
# TAGS: Math, Dynamic Programming, Combinatorics


class Solution:
    """
    DP Top-Down | Time and Space: O(M*N)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = dfs(i - 1, j) + dfs(i, j - 1)
            return memo[(i, j)]

        return dfs(m - 1, n - 1)

    """
    DP Bottom-Up
    """

    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


tests = [
    (
        (
            3,
            7,
        ),
        28,
    ),
    (
        (
            3,
            2,
        ),
        3,
    ),
]

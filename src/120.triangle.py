# Level: Medium
# TAGS: Array, Dynamic Programming

from typing import List


class Solution:
    # DP Top - Down | Time: O(N^2) | Space: O(N^2)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(triangle):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)

            memo[(i, j)] = min(lower_left, lower_right)
            return memo[(i, j)]

        return dfs(0, 0)

    # DP Bottom - Up | Time: O(N^2) | Space: O(N^2)
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[n - 1] = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                upper_left = triangle[i][j] + dp[i + 1][j]
                upper_right = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(upper_left, upper_right)

        return dp[0][0]


mi = 1
tests = [
    (
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],),
        11,
    ),
    (
        ([[-10]],),
        -10,
    ),
    (
        ([[-1], [2, 3], [1, -1, -3]],),
        -1,
    ),
]

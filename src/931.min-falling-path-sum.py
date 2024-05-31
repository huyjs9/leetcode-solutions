# Level: Medium
# TAGS: Array, Matrix, Dynamic Programming

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        for j in range(m):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(0, m):
                top_left = dp[i - 1][j - 1] if j - 1 >= 0 else float("inf")
                top_mid = dp[i - 1][j]
                top_right = dp[i - 1][j + 1] if j + 1 < m else float("inf")

                dp[i][j] = min(top_left, top_mid, top_right) + matrix[i][j]
        return min(dp[-1])


tests = [
    (
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]],),
        13,
    ),
    (
        ([[-19, 57], [-40, -5]],),
        -59,
    ),
]

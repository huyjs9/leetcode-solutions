from typing import List


class Solution:
    # Bottom - Up
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]

    # Top - Down
    def minPathSumTopDown(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = {}

        def pathSum(i, j):
            if i < 0 or j < 0:
                return float("inf")
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 and j == 0:
                return grid[0][0]

            min_path = min(pathSum(i - 1, j), pathSum(i, j - 1)) + grid[i][j]
            memo[(i, j)] = min_path

            return min_path

        return pathSum(n - 1, m - 1)


# solution = Solution().minPathSum
# print("7", solution([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
# print("12", solution([[1, 2, 3], [4, 5, 6]]))

tests = [
    (
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]],),
        7,
    ),
    (
        ([[1, 2, 3], [4, 5, 6]],),
        12,
    ),
]

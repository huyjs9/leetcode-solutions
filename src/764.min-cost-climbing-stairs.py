# Level: Medium
# TAGS: Array, Dynamic Programming

from typing import List


class Solution:
    # Bottom - Up
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[n - 1], dp[n - 2])

    # Top - Down
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def minCost(i):
            if i < 0:
                return float("inf")
            if i < 2:
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i] = min(minCost(i - 1), minCost(i - 2)) + cost[i]
            return memo[i]

        return min(minCost(n - 1), minCost(n - 2))


tests = [
    (
        ([10, 15, 20],),
        15,
    ),
    (
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],),
        6,
    ),
]

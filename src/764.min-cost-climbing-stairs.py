from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[n-1], dp[n-2])


solution = Solution().minCostClimbingStairs

print("15", solution([10, 15, 20]))
print("6", solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

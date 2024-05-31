from typing import List


class Solution:
    def minCostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        memo = {}

        def dfs(day):
            if day > 365:
                return 0
            if day in memo:
                return memo[day]
            if day in day_set:
                memo[day] = min(dfs(day + d) + c for d, c in zip([1, 7, 30], costs))
            else:
                memo[day] = dfs(day + 1)

            return memo[day]

        return dfs(1)

    def minCostTickets2(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)


tests = [
    (
        ([1, 4, 6, 7, 8, 20], [2, 7, 15]),
        11,
    ),
    (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]),
        17,
    ),
]

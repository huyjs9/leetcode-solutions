# Level: Medium
# TAGS: Array, Dynamic Programming

from typing import List


class Solution:
    # DP Bottom-Up | Time: O(N*T) | Space: O(T)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if t in memo:
                return memo[t]
            res = 0
            for j in range(n):
                res += dfs(t - nums[j])

            memo[t] = res
            return memo[t]

        return dfs(target)

    # DP Top-Down | Time: O(N*T) | Space: O(T)
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(n):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        return dp[target]


tests = [
    (
        (
            [1, 2, 3],
            4,
        ),
        7,
    ),
    (
        (
            [9],
            3,
        ),
        0,
    ),
]

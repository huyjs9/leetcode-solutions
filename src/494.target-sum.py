import collections
from typing import List


class Solution:
    """
    DP Top-Down
    Time and Space: O(N*T)
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, total):
            if i == len(nums):
                # is this the way to add/sub an item
                return 1 if total == target else 0
            if (i, total) in memo:
                return memo[(i, total)]

            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])

            return add + sub

        return dfs(0, 0)

    """
    DP Bottom-Up
    Time: O(N*T)
    Space: O(T)
    """

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            nxt = collections.defaultdict(int)

            for total in dp:
                nxt[total + num] += dp[total]
                nxt[total - num] += dp[total]
            dp = nxt

        return dp[target]


solution = Solution().findTargetSumWays2
print("5", solution([1, 1, 1, 1, 1], 3))
print("1", solution([1], 1))

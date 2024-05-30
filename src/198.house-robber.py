# Level: Medium
# TAGS: Array, Dynamic Programming

from typing import List


class Solution:
    # DP Top-Down | Time and Space: O(N)
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i < 0:
                return 0
            memo[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return memo[i]

        return dfs(len(nums) - 1)

    # DP Bottom-Up | Time and Space: O(N)
    def rob2(self, nums: List[int]) -> int:
        dp = [0, 0]
        for num in nums:
            dp.append(max(dp[-1], dp[-2] + num))
        return dp[-1]

    # Time: O(N) | Space: O(1)
    def rob3(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for num in nums:
            new = max(prev1, prev2 + num)
            prev2, prev1 = prev1, new
        return prev1


solution = Solution().rob
print("4", solution([1, 2, 3, 1]))
print("12", solution([2, 7, 9, 3, 1]))

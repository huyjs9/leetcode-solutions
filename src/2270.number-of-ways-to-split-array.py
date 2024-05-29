# Level: Medium
# TAGS: Array, Prefix Sum

from typing import List


class Solution:
    # Time: O(N) | Space: O(1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        left, right, n = 0, sum(nums), len(nums)

        cnt = 0
        for i, num in enumerate(nums):
            if i >= n - 1:
                return cnt

            left += num
            right -= num
            if left >= right:
                cnt += 1
        return cnt


solution = Solution().waysToSplitArray
print("2", solution([10, 4, -8, 7]))
print("2", solution([2, 3, 1, 0]))
print("1", solution([9, 9, 9]))
print("0", solution([-2, -1]))

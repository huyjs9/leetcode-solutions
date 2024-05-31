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


tests = [
    (
        ([10, 4, -8, 7],),
        2,
    ),
    (
        ([2, 3, 1, 0],),
        2,
    ),
    (
        ([9, 9, 9],),
        1,
    ),
    (
        ([-2, -1],),
        0,
    ),
]

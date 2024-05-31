# Level: Easy
# TAGS: Array, Prefix Sum

from typing import List


class Solution:
    # Time: O(N) | Space: O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num

        return -1


tests = [
    (
        ([1, 7, 3, 6, 5, 6],),
        3,
    ),
    (
        ([1, 2, 3],),
        -1,
    ),
    (
        ([2, 1, -1],),
        0,
    ),
]

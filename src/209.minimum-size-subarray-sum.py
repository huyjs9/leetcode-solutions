# Level: Medium
# TAGS: Array, Binary Search, Sliding Window, Prefix Sum

from typing import List


class Solution:
    # Time: O(N^2) | Space: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total, n = 0, 0, len(nums)

        min_len = float("inf")

        for right in range(n):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len


tests = [
    (
        (
            7,
            [2, 3, 1, 2, 4, 3],
        ),
        2,
    ),
    (
        (
            4,
            [1, 4, 4],
        ),
        1,
    ),
    (
        (
            11,
            [1, 1, 1, 1, 1, 1, 1, 1],
        ),
        0,
    ),
]

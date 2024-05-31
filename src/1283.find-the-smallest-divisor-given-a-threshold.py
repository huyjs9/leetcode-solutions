# Level: Medium
# TAGS: Array, Binary Search

from typing import List
from math import ceil


class Solution:
    # Time: O(N*logN) | Space: O(1)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_sum(div):
            return sum(ceil(num / div) for num in nums)

        lo, hi = 1, max(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if get_sum(mid) > threshold:
                lo = mid + 1
            else:
                hi = mid

        return lo


tests = [
    (
        (
            [1, 2, 5, 9],
            6,
        ),
        5,
    ),
    (
        (
            [44, 22, 33, 11, 1],
            5,
        ),
        44,
    ),
    (
        ([21212, 10101, 12121], 1000000),
        1,
    ),
]

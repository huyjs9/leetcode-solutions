# Level: Easy
# TAGS: Array, Hash Table

import collections
from typing import List


class Solution:
    # Time: O(N) | Space: O(N)
    def findShortestSubArray(self, nums: List[int]) -> int:
        counters = collections.Counter(nums)
        degree = max(counters.values())
        elements = [num for num, freq in counters.items() if freq == degree]

        first_i = {}
        last_i = {}
        for i, num in enumerate(nums):
            if num not in first_i:
                first_i[num] = i
            last_i[num] = i
        return min(last_i[num] - first_i[num] + 1 for num in elements)

    # Time: O(N) | one pass --> this solution only uses 1 loop
    def findShortestSubArray2(self, nums: List[int]) -> int:
        first, count, ans, degree = {}, {}, 0, 0
        for i, num in enumerate(nums):
            """
            same as the way to set `first_i` in the first solution,
            it means:
              if the exist, take no effect
              if the key does not exist, set the value to the key
            """
            first.setdefault(num, i)
            """
            same as the collection.Counters
            """
            count[num] = count.get(num, 0) + 1

            if count[num] > degree:
                degree = count[num]
                ans = i - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - first[num] + 1)

        return ans


tests = [
    (
        ([1, 2, 2, 3, 1],),
        2,
    ),
    (
        ([1, 2, 2, 3, 1, 4, 2],),
        6,
    ),
]

# Level: Medium
# TAGS: Array, Two Pointers, Sorting

from typing import List


class Solution:
    # Hash map | Time and Space: O(N)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = {0: 0, 1: 0, 2: 0}

        for _, num in enumerate(nums):
            counter[num] = counter.get(num) + 1

        zero, one, two = counter.get(0), counter.get(1), counter.get(2)
        for z in range(zero):
            nums[z] = 0
        for o in range(zero, zero + one):
            nums[o] = 1
        for t in range(zero + one, zero + one + two):
            nums[t] = 2

        return nums  # for local testing only

    # Two pointers | Time: O(N) | Space: O(1)
    def sortColors1(self, nums: List[int]) -> None:
        # red - 0, white - 1, blue - 2
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
        return nums


tests = [
    (
        ([2, 0, 2, 1, 1, 0],),
        [0, 0, 1, 1, 2, 2],
    ),
    (
        ([2, 0, 1],),
        [0, 1, 2],
    ),
    (
        ([0],),
        [0],
    ),
]

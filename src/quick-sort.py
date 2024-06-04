from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums: List[int], start: int, end: int) -> List[int]:
        if start >= end:
            return nums

        pivot_index = self._partition(nums, start, end)

        self._quick_sort(nums, start, pivot_index - 1)
        self._quick_sort(nums, pivot_index, end)

        return nums

    def _partition(self, nums: List[int], start: int, end: int) -> int:
        mid = start + (end - start) // 2

        pivot = nums[mid]

        while start <= end:
            if nums[start] < pivot:
                start += 1
            elif nums[end] > pivot:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        return start


tests = [
    (
        ([5, 2, 3, 1],),
        [1, 2, 3, 5],
    ),
    (
        ([1, 7, 4, 1, 10, 9, -2],),
        [-2, 1, 1, 4, 7, 9, 10],
    ),
]

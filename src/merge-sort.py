from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        return self._merge_sort(nums)

    def _merge_sort(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return nums

        start, end = 0, len(nums)

        mid = start + (end - start) // 2
        print(mid)

        left_nums = nums[:mid]
        right_nums = nums[mid:end]

        return self._merge(
            self._merge_sort(left_nums),
            self._merge_sort(right_nums),
        )

    def _merge(self, left_nums: List[int], right_nums: List[int]) -> List[int]:
        left_index, right_index = 0, 0
        result = []

        while left_index < len(left_nums) and right_index < len(right_nums):
            if left_nums[left_index] < right_nums[right_index]:
                result.append(left_nums[left_index])
                left_index += 1
            else:
                result.append(right_nums[right_index])
                right_index += 1

        print(result, left_index, right_index, left_nums, right_nums)

        result.extend(left_nums[left_index:])
        result.extend(right_nums[right_index:])

        return result


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

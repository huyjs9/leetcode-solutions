# Level: Medium
# TAGS: Array

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        return intervals


# solution = Solution().insert
# print([[1, 5], [6, 9]], "***", solution([[1, 3], [6, 9]], [2, 5]))
# print(
#     [[1, 2], [3, 10], [12, 16]],
#     "***",
#     solution([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
# )

tests = [
    (
        (
            [[1, 3], [6, 9]],
            [2, 5],
        ),
        [[1, 5], [6, 9]],
    ),
    (
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
        ),
        [[1, 2], [3, 10], [12, 16]],
    ),
]

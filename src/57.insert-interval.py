# Level: Medium
# TAGS: Array

from typing import List


class Solution:
    # DP | Time and Space: O(N)
    # Ref: https://leetcode.com/problems/insert-interval/solutions/4885946/beat-97-22-full-explanation-with-pictures/
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1
        merged.append(newInterval)

        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

    # Time and Space: O(N)
    # Author: lee215
    def insert2(self, intervals, newInterval):
        s, e = newInterval
        parts = merge, left, right = [], [], []
        for i in intervals:
            # Very pythonic.
            # 0 when both are False,
            # 1 when left is correct,
            # -1 when right is correct.
            parts[(i[-1] < s) - (i[0] > e)].append(i)
        if merge:
            s = min(s, merge[0][0])
            e = max(e, merge[-1][-1])
        return left + [[s, e]] + right


mi = 0
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

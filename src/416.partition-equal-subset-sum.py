# Level: Medium
# TAGS: Array, Dynamic Programming

from typing import List


class Solution:
    """
    DP Bottom-Up | Hash map
    Time: O(N*T) | Space: O(T) with N is len(nums), T is target
    Ref: https://leetcode.com/problems/partition-equal-subset-sum/solutions/462699/whiteboard-editorial-all-approaches-explained/
    """

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        visited = set([0])
        for _, num in enumerate(nums):
            visited |= {j + num for j in visited}
        return target in visited

    """
    DP Bottom-Up | Backtracking
    Time: O(N*T) | Space: O(T) with N is len(nums), T is target
    Choose current number or next number
    """

    def canPartition1(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        memo = {}

        def dfs(i, sofar):
            if i == len(nums) or sofar > target:
                return False
            if sofar == target:
                return True
            if (i, sofar) in memo:
                return memo[(i, sofar)]

            memo[(i, sofar)] = dfs(i + 1, sofar + nums[i]) or dfs(i + 1, sofar)

            return memo[(i, sofar)]

        return dfs(0, 0)


tests = [
    (
        ([1, 5, 11, 5],),
        True,
    ),
    (
        ([1, 2, 3, 5],),
        False,
    ),
]

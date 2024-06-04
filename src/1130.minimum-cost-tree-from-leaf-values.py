# Level: Medium
# TAGS: Array, Dynamic Programming, Stack, Greedy, Monotonic Stack

from typing import List


class Solution:
    """
    DP Top-Down
    Time: O(N^3) | Space: O(N)
    """

    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        memo = {}

        def findNext(start, end):
            if start == end:
                return 0

            if (start, end) in memo:
                return memo[(start, end)]

            res = float("inf")
            for i in range(start, end):
                rootVal = max(arr[start : i + 1]) * max(arr[i + 1 : end + 1])
                res = min(
                    res,
                    rootVal + findNext(start, i) + findNext(i + 1, end),
                )

            memo[(start, end)] = res
            return res

        return findNext(0, n - 1)

    """
    DP Bottom-Up
    Time: O(N^3) | Space: O(N)
    """

    def mctFromLeafValues1(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for distance in range(2, n + 1):
            for start in range(n - distance + 1):
                end = start + distance - 1

                for i in range(start, end):
                    rootVal = max(arr[start : i + 1]) * max(arr[i + 1 : end + 1])
                    dp[start][end] = min(
                        dp[start][end], rootVal + dp[start][i] + dp[i + 1][end]
                    )
        return dp[0][-1]

    """
    DP | Time: O(N^2) | Space: O(N)
    Remove the element form the smallest to bigger
    For each element a, cost = min(left, right) * a

    Ref: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/339959/one-pass-o-n-time-and-space/
    """

    def mctFromLeafValues2(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1 : i] + arr[i + 1 : i + 2]) * arr.pop(i)
        return res

    """
    One pass solution from lee215
    Stack | Time and Space: O(N)
    Just find the next greater element in the array, on the left and one right.
    """

    def mctFromLeafValues3(self, arr: List[int]) -> int:
        res = 0
        stack = [float("inf")]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


tests = [
    (
        ([6, 2, 4],),
        32,
    ),
    (
        ([4, 11],),
        44,
    ),
]

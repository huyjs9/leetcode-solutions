# Level: Medium
# TAGS: Array, Dynamic Programming, Matrix

from typing import List


class Solution:
    # Greedy approach
    """
    ref: https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/

    1  1
    1 [1]
    Find the min of top, left, top-left if the current is 1
    1  1
    1 [2]
    It means: min(1,1,1) + 1 = 2

    Another example
    1  1
    0 [1]

    It will be:
    1  1
    0 [1]
    It means: min(1,1,0) + 1 = 1


    Time: O(R*C) | Space: O(1)
    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        matrix = [[1 if r == "1" else 0 for r in row] for row in matrix]
        R, C = len(matrix), len(matrix[0])

        max_side = 0

        for i in range(0, R):
            if matrix[i][0]:
                max_side = 1
        for i in range(0, C):
            if matrix[0][i]:
                max_side = 1

        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][c]:
                    matrix[r][c] = (
                        min(matrix[r - 1][c], matrix[r - 1][c - 1], matrix[r][c - 1])
                        + 1
                    )
                    max_side = max(max_side, matrix[r][c])

        return max_side**2


solution = Solution().maximalSquare
print(
    "4",
    solution(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    ),
)
print("1", solution([["0", "1"], ["1", "0"]]))
print("0", solution([["0"]]))
print("1", solution([["1"]]))

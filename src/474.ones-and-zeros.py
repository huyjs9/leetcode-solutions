import collections
from typing import List


class Solution:
    # Recursive DFS Top-Down | Time & Space: O(M*N*L) with L is the length of strs
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, zeros, ones):
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]

            if zeros < 0 or ones < 0:
                return float("-inf")
            if i == len(strs):
                return 0

            skip = dfs(i + 1, zeros, ones)

            zero, one = counters[i]["0"], counters[i]["1"]
            take = dfs(i + 1, zeros - zero, ones - one) + 1

            pick = max(skip, take)
            memo[(i, zeros, ones)] = pick
            return pick

        # * create `counters using collections.Counter
        counters = [collections.Counter(s) for s in strs]
        return dfs(0, m, n)

    # DP Bottom-Up | Time & Space: O(M*N*L)
    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # * create `counters using array
        counters = [[s.count("0"), s.count("1")] for s in strs]

        for zero, one in counters:
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)

        return dp[m][n]


tests = [
    (
        (
            ["10", "0001", "111001", "1", "0"],
            5,
            3,
        ),
        4,
    ),
    (
        (
            ["10", "0", "1"],
            1,
            1,
        ),
        2,
    ),
]

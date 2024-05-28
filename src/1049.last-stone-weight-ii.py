from typing import List


class Solution:
    """
    DP Bottom-Up using set
    S=sum(stones): Time O(N*S) | Space O(S)
    """

    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}  # dp = set([0])
        for a in stones:
            dp = {a + x for x in dp} | {abs(a - x) for x in dp}
            # dp = set([a + x for x in dp] + [abs(a - x) for x in dp])

        return min(dp)

    """
    Recursive memoization using knapsack.
    Time and Space: O(N * S * S)
    """

    def lastStoneWeightII2(self, stones: List[int]) -> int:
        memo = {}

        def dfs(i, sumL, sumR):
            if i == len(stones):
                return abs(sumL - sumR)
            if (i, sumL, sumR) in memo:
                return memo[(i, sumL, sumR)]

            stone = stones[i]
            memo[(i, sumL, sumR)] = min(
                dfs(i + 1, sumL + stone, sumR), dfs(i + 1, sumL, sumR + stone)
            )
            return memo[(i, sumL, sumR)]

        return dfs(0, 0, 0)


solution = Solution().lastStoneWeightII2
print("1", solution([1, 2, 4]))
print("1", solution([2, 7, 4, 1, 8, 1]))
print("5", solution([31, 26, 33, 21, 40]))

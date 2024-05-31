# Level: Easy
# TAGS: Dynamic Programming


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n: int):
            if n == 0 or n == 1:
                return 1
            if n not in memo:
                memo[n] = dfs(n - 1) + dfs(n - 2)

            return memo[n]

        return dfs(n)


tests = [
    (
        (4,),
        5,
    ),
]

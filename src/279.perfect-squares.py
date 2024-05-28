class Solution:
    # DP Bottom-Up | Time O(N*log(N)) | Space O(N) 5168ms
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            if i < 0:
                return float("inf")

            memo[i] = float("inf")
            sqs = [i**2 for i in range(1, int(i**0.5) + 1)]

            for sq in sqs:
                memo[i] = min(memo[i], 1 + dfs(i - sq))

            return memo[i]

        return dfs(n)

    # DP Top-Down | Time O(N*log(N)) | Space O(N) 2758ms
    def numSquares2(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            sqs = [i**2 for i in range(1, int(i**0.5) + 1)]
            for sq in sqs:
                dp[i] = min(dp[i], 1 + dp[i - sq])
        return dp[n]


solution = Solution().numSquares2
print("3", solution(12))
print("2", solution(13))

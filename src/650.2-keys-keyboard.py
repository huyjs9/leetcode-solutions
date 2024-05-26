class Solution:
    # Math
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i + self.minSteps(n // i)
        return n

    # DP
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = i
            for j in range(1, i):
                # if sequence of length 'j' can be pasted multiple times to get length 'i' sequence
                if i % j == 0:
                    """
                      - we just need to paste sequence j (i//j - 1) times, hence additional (i//j) times since we need to copy it first as well.
                      - we don't need checking any smaller length sequences 
                    """
                    dp[i] = dp[j] + i//j
        return dp[n]


solution = Solution().minSteps
print("3", solution(3))
print("0", solution(1))

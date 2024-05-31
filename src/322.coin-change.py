# Level: Medium
# TAGS: Array, Dynamic Programming, Breadth-First Search

from typing import List


class Solution:
    # BFS | Time and Space: O(A*N) where A is the amount and N is the number of coins
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return amount

        visited = set()

        q = [(amount, 1)]
        for amount, step in q:
            if amount in visited:
                continue
            visited.add(amount)
            for coin in coins:
                if coin == amount:
                    return step
                if coin < amount:
                    q.append((amount - coin, step + 1))
        return -1

    # DP - Bottom-Up | Time: O(A*N) | Space: O(A)
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if i == coin:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[i - coin] + dp[coin])
        return dp[amount] if dp[amount] != float("inf") else -1


solution = Solution().coinChange2
print("3", solution([1, 2, 5], 11))
print("-1", solution([2], 11))
print("0", solution([1], 0))

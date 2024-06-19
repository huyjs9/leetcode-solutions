# Level: Medium
# TAGS: Math, Dynamic Programming, Probability and Statistics


class Solution:
    # DP Top-Down | Time and Space: O(N^2)
    def soupServings(self, n: int) -> float:
        """
        print(dfs(1000,1000))            # 0.9765650521094358
        print(dfs(10000,10000))          # 0.9999999999159161
        for i in range(1000,10000):
            if 1-dfs(i,i) <= 10**(-5):
                print(i)                 # 4451
                break
        """
        if n >= 4451:
            return 1

        memo = {}

        def dfs(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0 and j > 0:
                return 1
            if i > 0 and j <= 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            p1 = dfs(i - 100, j)
            p2 = dfs(i - 75, j - 25)
            p3 = dfs(i - 50, j - 50)
            p4 = dfs(i - 25, j - 75)

            memo[(i, j)] = 0.25 * (p1 + p2 + p3 + p4)
            return memo[(i, j)]

        return dfs(n, n)


tests = [
    (
        (50,),
        0.62500,
    ),
    (
        (100,),
        0.71875,
    ),
]

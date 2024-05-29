# Level: Medium
# TAGS: Array, Binary Search


from typing import List
import math


class Solution:
    # Time: O(N*log(M)) w/ M = max(piles) | Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)

            return total <= h

        total = sum(piles)
        lo, hi = math.ceil(total / h), max(piles)
        while lo < hi:
            # This is the second way to find the mid to prevent overflow
            mid = lo + (hi - lo) // 2

            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


solution = Solution().minEatingSpeed
print("4", solution([3, 6, 7, 11], 8))
print("30", solution([30, 11, 23, 4, 20], 5))
print("23", solution([30, 11, 23, 4, 20], 6))

# Level: Medium
# TAGS: Array, Hash Table, Math, Bit Manipulation, Prefix Sum


from typing import List


class Solution:
    """
    i < j <= k
    ref: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/solutions/623747/JavaC++Python-One-Pass-O(N4)-to-O(N)/
    """

    # Time: O(N^3) | Space: O(N)
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)

        cnt = 0
        for i in range(1, len(prefix)):
            for j in range(i + 1, len(prefix)):
                for k in range(j, len(prefix)):
                    a = prefix[i - 1] ^ prefix[j - 1]
                    b = prefix[j - 1] ^ prefix[k]
                    if a == b:
                        cnt += 1

        return cnt

    """
    prefix[i] = arr[0]^arr[1]^...arr[i-1]
    prefix[k] = arr[0]^arr[1]^...arr[i-1]^arr[i]^...arr[k-1]
    
    prefix[i] == prefix[k+1] => prefix[i]^prefix[k+1] = 0 = arr[i]^...arr[k-1]
    
    it means all elements in array from `i` to `k-1` XOR each other will be 0
    
    so, we will count all `j` from `i` to `k-1`
    
    Time: O(N^2) | Space: O(N)
    """

    def countTriplets2(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)

        cnt = 0
        for i in range(0, len(prefix)):
            for k in range(i + 1, len(prefix)):
                if prefix[i] == prefix[k]:
                    cnt += k - 1 - i
        return cnt

    """
    (i - 1 - i1) + (i - 1 - i2) + (i - 1 - i3) + ...
    = f*(i - 1) - (i1 + i2 + i3 + ...)
    w/ f is number of prefix[i] == prefix[k]
    Time: O(N) | Space: O(N)
    """

    def countTriplets3(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)

        cnt = 0
        count = {}
        total_i = {}
        for i in range(0, len(prefix)):
            cur = prefix[i]
            count_cur = count.get(cur, 0)
            total_i_cur = total_i.get(cur, 0)

            cnt += count_cur * (i - 1) - total_i_cur
            count[cur] = count_cur + 1
            total_i[cur] = total_i_cur + i

        return cnt


tests = [
    (
        ([2, 3, 1, 6, 7],),
        4,
    ),
    (
        ([1, 1, 1, 1, 1],),
        10,
    ),
]

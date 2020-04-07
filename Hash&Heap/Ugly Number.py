"""
lintcode 4: Ugly Number

Ugly number is a number that only have prime factors 2, 3 and 5.
Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
Note that 1 is typically treated as an ugly number.

Example 1:
Input: 9
Output: 10
"""

import heapq 
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber1(self, n):
        # write your code here
        if n <= 6:
            return n

        res = [0 for i in range(n)]
        res[0] = 1 
        a, b, c = 0, 0, 0 

        for i in range(1, n):
            res[i] = min(res[a]*2, res[b]*3, res[c]*5)
            if (res[i] == res[a]*2):
                a += 1
            if (res[i] == res[b]*3):
                b += 1 
            if (res[i] == res[c]*5):
                c += 1 
        return res[n - 1]
    
    def nthUglyNumber2(self, n):
        heap = [1]
        visited = set([1])
        value = None
        for i in range(n):
            value = heapq.heappop(heap) 
            for factor in [2, 3, 5]:
                if value * factor not in visited:
                    visited.add(value * factor)
                    heapq.heappush(heap, value * factor)
        return value
    # O(nlogn)

if __name__ == "__main__":
    n = 29
    print(Solution().nthUglyNumber1(n))
    print(Solution().nthUglyNumber2(n))

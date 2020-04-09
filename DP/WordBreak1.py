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
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        # create len(s)+1 array, inital it as true,
        # dp[i] means in s the ended in ith charater can be divide into arra in dict, 
        # return dp[-1].
        # dp[i] =dp[j] and dp[j:i] in dict, 0<=j<i
        if not s:
            return True
        
        length = len(s)
        dp = [False for i in range(length + 1)]
        dp[0] = True
        for i in range(1, length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break 

        return dp[-1]
        
if __name__ == "__main__":
    s = "applepenapple"   
    dict = ["apple","pen"]
    print(Solution().wordBreak(s,dict))

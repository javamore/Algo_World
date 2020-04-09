"""
lintcode 107: WordBreak1

Given a string s and a dictionary of words dict,
determine if s can be broken into a space-separated sequence of one or more dictionary words.

Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

Example 2:
	Input: "a", ["a"]
	Output:  true
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

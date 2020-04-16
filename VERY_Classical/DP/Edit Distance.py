"""
lintcode 119 Edit Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. 
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: 
"horse"
"ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        m, n = len(word1), len(word2)
        #(m,n) matrix
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #initial value
        for i in range(m + 1): dp[i][0] = i 
        for j in range(n + 1): dp[0][j] = j 
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                               dp[i-1][j] + 1,
                               dp[i][j-1] + 1)
                               
        return dp[m][n]

if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'rose'
    print(Solution().minDistance(word1,word2))

"time:O(m*n), space:O(m*n)->O(min(m,n))"


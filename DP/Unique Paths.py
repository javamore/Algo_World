"""
lintcode 114: Unique Paths

A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Example:
Input:  n = 3, m = 3
Output: 6	
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # optimized: becasuse every row rely on the last row, so we can use rolling array.
    # dp[j] = dp[j-1] + dp[j]

    def uniquePaths(self, m, n):
        # write your code here
        dp = [0 for j in range(n)]
        dp[0] = 1 
        
        for i in range(m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
                
        return dp[n - 1]
        
if __name__ == "__main__":
    m = 3
    n = 3
    print(Solution().uniquePaths(m, n))
    
#time: O(m*n)  space: O(n)

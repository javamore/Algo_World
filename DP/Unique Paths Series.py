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

class Solution1:
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
    print(Solution1().uniquePaths(m, n))
    
#time: O(m*n)  space: O(n)



"""
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Example 1:
	Input: [[0]]
	Output: 1
Example 2:
	Input:  [[0,0,0],[0,1,0],[0,0,0]]
	Output: 2
"""

class Solution2:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid or len(obstacleGrid) == 0 or not obstacleGrid[0] or len(obstacleGrid[0]) == 0:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for j in range(n)]
        dp[0] = 1 
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0 
                    continue
                
                if i > 0 and j > 0:
                    dp[j] += dp[j - 1]
                    continue
                
                if j > 0:
                    dp[j] = dp[j - 1]
        
        return dp[n - 1]



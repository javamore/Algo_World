"""
lintcode 77 Longest Common Subsequence
Given two strings, find the longest common subsequence (LCS).
Your code should return the length of LCS.

Example 1:
	Input:  "ABCD" and "EDCA"
	Output:  1
	
	Explanation:
	LCS is 'A' or  'D' or 'C'

Example 2:
	Input: "ABCD" and "EACB"
	Output:  2
	
	Explanation: 
	LCS is "AC"
"""

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for i in range(m+1)]
 
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + (1 if A[i-1] == B[j-1] else 0) )
        return dp[m][n]


if __name__ == '__main__':
    A = 'EABCEDA'
    B = 'EBECDA'
    print(Solution().longestCommonSubsequence(A,B))




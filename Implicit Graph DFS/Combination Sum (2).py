""" 
lintcode 153
Given an array num and a number target. Find all unique combinations in num where the numbers sum to target.

1.Each number in num can only be used once in one combination.
2.All numbers (including target) will be positive integers.
3.Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
4.Different combinations can be in any order.
5.The solution set must not contain duplicate combinations. repeated number may be chosen from candidates unlimited number of times.


Input: num = [7,1,2,5,1,6,10], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Input: num = [1,1,1], target = 2
Output: [[1,1]]
Explanation: The solution set must not contain duplicate combinations.

"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted((candidates))
        combination = []
        result = []
        start = 0
        self.dfs(candidates, target, start,combination, result)
        return result
    
    def dfs(self, candidates, target, start, combination, result):
        if target < 0:
            return
        
        # when target == 0 is the exit of recursion. 
        if target == 0:
            result.append(combination[:])
            return 

        # when target - candidates[i] < 0, exit the recursion.
        for i in range(start, len(candidates)):

            if candidates[i] > target:
                return 
            if i > start and candidates[i] == candidates[i-1]:
                continue

            combination.append(candidates[i])
            # because we can not duplicate, so start from "i + 1", if not, "i"
            self.dfs(candidates, target - candidates[i], i + 1, combination, result)
            # backtracking 
            combination.pop()
            
            
                
if __name__ == '__main__':

    candidates = [7,1,2,5,1,6,10]
    target = 8
    print(Solution().combinationSum(candidates,target))


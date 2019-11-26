""" 
lintcode 135
Given a set of candidtate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

1.All numbers (including target) will be positive integers.
2.Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
3.Different combinations can be in any order.
4.The solution set must not contain duplicate combinations.

Example:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]

Example2:
Input: candidates = [1], target = 3
Output: [[1, 1, 1]]

"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # sort and eliminate duplications first
        candidates = sorted(list(set(candidates)))
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, candidates, target, start, combination, result):
        if target < 0:
            return
        
        # when target == 0 is the exit of recursion. 
        if target == 0:
            #do deepcopy
            clone = list(combination)
            result.append(clone)
            #print(id(clone), clone)
            return 

        # when target - candidates[i] < 0, exit the recursion.
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            # because we can duplicate, so start from "i", if not, "i + 1 "
            self.dfs(candidates, target - candidates[i], i, combination, result)
            # backtracking 
            combination.pop()
            
            
                
if __name__ == '__main__':
    candidates =[1]
    target = 3
    #    candidates =[2,3,6,7]
    #    target = 7
    print(Solution().combinationSum(candidates,target))


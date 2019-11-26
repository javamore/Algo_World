""" 
lintcode 18
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        combinations = []
        self.dfs(nums, 0 ,[], combinations)
        return combinations
        
    # Defination of this recursion: 
    # To find all start with "combination"'s combinations,
    # then put into combinations.
    # The other candidates were put into index , the rest were picked from nums[index].
    
    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))
        
        for i in range(index, len(nums)): 

            # to eliminate duplication. 
            if i != index and nums[i] == nums[i - 1]:
                continue

            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()
            
 # except line 45, in order to eliminate duplication, rest are same as 
 # first subset problem (problem 17).
            
 
if __name__ == '__main__':
    a =[1,2,2]
    print(Solution().subsetsWithDup(a))


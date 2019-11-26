""" 
lintcode 17
Given a set of distinct integers, return all possible subsets.
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
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
    #[1,2....] -> [1,2,3]
    #[1,2....] -> [1,2,4]
    #.........
        for i in range(index, len(nums)): #for loop [3,4,5.....]
    #when for loop "3", append 3 intto combinations, then 
    #find all combinations which start with [1,2,3]....
            combination.append(nums[i])
    #i+1 because if picked one, then pick next one, which is i+1 in index
            self.dfs(nums, i + 1, combination, combinations)
    #we have to pop "3", or we will have "3" in the further combinations
            combination.pop()
        
        #exit is here
        
            
if __name__ == '__main__':
    a =[1,2,2]
    print(Solution().subsets(a))


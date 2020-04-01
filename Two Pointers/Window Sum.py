"""
lintcode 604 Window Sum
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, 
find the sum of the element inside the window at each moving.

Example 1
Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
"""

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        #check input 
        if not nums or k == 0:
            return [] 
            
        #inital sum 
        sums = 0
        for i in range (k):
            sums += nums[i]
            
        # using two pinters
        result = [sums]
        left, right = 0, k 
        while right < len(nums):
            #pop left and append right then move forward.
            sums = sums - nums[left] + nums[right]
            left += 1 
            right += 1 
            result.append(sums)
        return result 
        
if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    k = 3
    print(Solution().winSum(nums,k))
        
        

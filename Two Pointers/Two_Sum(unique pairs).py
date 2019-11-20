""" 
lintcode 587
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. 
Please return the number of pairs.
Example 1:
Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:
Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
    
        nums.sort()
        count = 0 
        j, k = 0, len(nums) - 1 

        while j < k:

            if nums[j] + nums[k] == target:
                count += 1 
                j += 1 
                k -= 1 
                # avoid duplication, using while loop to jump the same elements, nums[j] == nums[j-1] 
                while j < k and nums[j] == nums[j - 1]:
                    j += 1 
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1 
        
            elif nums[k] + nums[j] > target:
                k -= 1
            else:
                j += 1
                
        return count

if __name__ == '__main__':
    nums =[1,1,2,45,46,46]
    target = 47
    # 1+46=47, 2+45=47
    
    nums1 =[-2,-2,1,1,0]
    target1 = 1

    print(Solution().twoSum6(nums, target))
    print(Solution().twoSum6(nums1, target1))

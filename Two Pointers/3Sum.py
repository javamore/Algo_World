""" 
lintcode 57
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Example 1:
Input:[2,7,11,15]
Output:[]

Example 2:
Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
Notice

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    #asuume a + b = -c or -a = b + c 
    def threeSum(self, nums):
        # write your code here
        nums.sort()
        results = []
        length = len(nums)
        # avoid duplications
        for i in range(0, length-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue #jump, ignore it.
            self.two_sum(nums,i+1, length-1, -nums[i], results)
            #tagret is -nums[i], i start from i+1 
        return results
    
    def two_sum(self,nums,left,right,target,results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                left += 1 
                right -= 1 
                while left < right and nums[left] == nums[left - 1]:
                    left += 1 
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1 
            elif nums[left] + nums[right] > target:
                right -= 1 
            else:
                left += 1 

if __name__ == '__main__':
    nums1 =[1,1,2,45,-46,46]
    nums2 = [2,7,11,15]
    nums3 = [-1,0,1,2,-1,-4]

    print(Solution().threeSum(nums1))
    print(Solution().threeSum(nums2))
    print(Solution().threeSum(nums3))


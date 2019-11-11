
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        pivot = nums[-1]
        while start + 1 < end:  #control interval
            mid = (start + end) // 2
            if nums[mid] <= pivot:   ##if value of mid <= pivot, the interval move forward left side.
                end = mid
            else:
                start = mid
        return min(nums[start],nums[end]) ##return the min of nums[start], nums[end]

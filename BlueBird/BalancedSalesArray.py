class Solution:
      def BalancedSalesArray(self, sales):
        # write your code here
        if not sales:
            return 0 
        n = len(sales)
        left_sum, right_sum = 0, 0
        left, right = 0, n - 1     
        while left <= right:
            if left_sum and left_sum == right_sum:
                return left
            
            if not left_sum or (left_sum < right_sum):
                left_sum += sales[left]
                left += 1
            if left_sum > right_sum:
                right_sum += sales[right]
                right -= 1
        return -1

if __name__ == '__main__':
    A = (1,2,3,4,6)
    print(Solution().BalancedSalesArray(A))



"""
Approach 1, space:O(1), Time:O(n)

Another tricky Solution:
class Solution:
    def pivotIndex(self, nums):
        
        :type nums: List[int]
        :rtype: int
        
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1

Another Solution:

           for index in range(len(sales)):
            if sum(sales[0:index]) == sum(sales[index + 1: len(sales)]):
                return index
            time: O(n^2), space:O(1)
"""


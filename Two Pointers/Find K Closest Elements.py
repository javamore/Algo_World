'''
lintcode 460 Find K Closest Elements
Given target, a non-negative integer k and an integer array A sorted in ascending order, 
find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
Otherwise, sorted in ascending order by number if the difference is same.
1)The value k is a non-negative integer and will always be smaller than the length of the sorted array.
2)Length of the given array is positive and will not exceed 10^4
3)Absolute value of elements in the array will not exceed 10^4

​​Example 1:
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:
Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]

Challenge
O(logn + k) time
'''

def bisect(nums, target):
    
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1 
    return lo
#or you can: from bisect import bisect
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        m = bisect(A, target)
        left = m
        right = m
        output = []
        #using bisect to find the first element is greater than target.
        while k > 0 and left > 0 and right < len(A):
            if (right >= len(A)) or (left >= 0 and abs(A[left-1] - target) <= abs(A[right] - target)):
                output.append(A[left-1])
                left -= 1
            else:
                output.append(A[right])
                right += 1
            k -= 1
        #return A[left + 1: right]
        if k:
            if left > 0:
                output.extend(A[left - k:left][::-1])
            if right < len(A):
                output.extend(A[right:right + k])
        return output

if __name__ == "__main__":
    print(Solution().kClosestNumbers([1,2,3,4,4,7], 5.2, 2))
    print(Solution().kClosestNumbers([1,2,3,4,4,7], 6.5, 3))
    print(Solution().kClosestNumbers([1,2,3,4,4,6,6], 5, 3))
    print(Solution().kClosestNumbers([1,2,3], 2, 3))
    print(Solution().kClosestNumbers([1,4,6,8], 3, 3))
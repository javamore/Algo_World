""" 
lintcode 75
There is an integer array which has the following features:
The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:
A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.
"""

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        low, high = 0, len(A)-2
        
        while low <= high:
            mid = (low + high)//2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        
        if A[high] >= A[low]:
            return high
        else:
            return low

if __name__ == '__main__':
    A = (1,2,3,4,5,8,7,6)
    print(Solution().findPeak(A))

"""
Find the k smallest numbers in a data stream of length n (k<<n),
using only O(k) space (the stream itself might be too big to fit in memory).

>>> ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
[2, 3, 5, 7]
>>> ksmallest(3, range(1000000, 0, -1))
[1, 2, 3]

Note: 
a) it should work with both lists and lazy lists
b) the output list should be sorted

Q: What is your complexity? Write down the detailed analysis in report.txt.
A: For each element we push into heap, using O(log(k)). Total time T(n)= O(k+(n-k)logk*2+klogk)=O(2nlogk-klogk+k) = O(nlogk)

Filename: datastream.py

[UPDATE] The built-in function heapq.nsmallest() is _not_ allowed for this problem.
    The whole point is to implement it yourself. :)

"""
import heapq
import time 

def ksmallest(k,a):
    if k == 0 or len(a) == 0:
        return []

    h = []
    heapq.heapify(h)
    #h = [-x for x in a[:k]]
    for x in a:
        if len(h) < k:
            heapq.heappush(h, -x)
        elif -x > h[0]:
            heapq.heapreplace(h, -x)
    #return sorted ([-x for x in h])
    return [-x for x in heapq.nlargest(k, h)]
#------------------------------------------------------------------------------------------
def klargest(k,a):
    if k == 0 or len(a) == 0:
        return []
        
    h = []
    heapq.heapify(h)
    #h = [x for x in a[:k]]
    for x in a:
        if len(h) < k:
            heapq.heappush(h, x)
        elif x > h[0]:
            heapq.heapreplace(h, x)
    #return sorted ([x for x in h])
    return [x for x in heapq.nlargest(k, h)]
#------------------------------------------------------------------------------------------
def funnyklargest(k,a):
    heapq.heapify(a)
    topk = heapq.nlargest(k, a)
    topk.sort()
    topk.reverse()
    return topk 
#time: O(nlogk)

#------------------------------------------------------------------------------------------
# using quick select, but no need to return Kth number, just select K numbers.
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        self.quick_select(nums, 0, len(nums) - 1, k)
        res = nums[:k]
        res.sort(reverse=True)
        return res
        
        
    def quick_select(self, nums, left, right, k):
        if left == right:
            return
        pivot = nums[left]
        i, j = left, right
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if j - left + 1 >= k:
            self.quick_select(nums, left, j, k)
        if i - left + 1 <= k:
            self.quick_select(nums, i, right, k - (i - left))
#------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    print(ksmallest(12, range(1000000, 0, -2)))

    print(klargest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    print(klargest(12, range(1000000, 0, -2)))
    print(funnyklargest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    print(Solution().topk([10, 2, 9, 3, 7, 8, 11, 5, 7], 4))

        
      
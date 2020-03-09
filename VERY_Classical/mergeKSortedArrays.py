"""
Lintcode 486 Merger K sorted arrays

Given k sorted integer arrays, merge them into one sorted array.
Example:
Input: 
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""


import heapq
class Solution:

    def mergeKSortedArrays(self,arrays):
        res = []
        heap = []

        for index, array in enumerate(arrays):
            if len(array) == 0 :
                continue
            heapq.heappush(heap, (array[0], index, 0))

        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            res.append(val)
            if  y + 1 < len(arrays[x]):
                heapq.heappush(heap,(arrays[x][y + 1], x, y + 1))
        
        return res 
#fastest version time: O(NlogK), space:O(k)

#--------------------------------------------------------------------------------------------------------------------
#top-down, divide and conquer
    def mergekKSortedArrays2(self, arrays):
        return self.merge_range_arrays(arrays, 0, len(arrays) - 1)
        
    def merge_range_arrays(self, arrays, start, end):
        if start == end:
            return arrays[start]
        
        mid = (start + end) // 2
        left = self.merge_range_arrays(arrays, start, mid)
        right = self.merge_range_arrays(arrays, mid + 1, end)
        return self.merge_two_arrays(left, right)
        
    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array

#---------------------------------------------------------------------------------------------------------------------------------

#bottom-up two-two merge 
    def mergeKSortedArrays3(self, arrays):
        while len(arrays) > 1:
            next_arrays = []
            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    array = self.merge_two_arrays(arrays[i], arrays[i + 1])
                else:
                    array = arrays[i]
                next_arrays.append(array)
            arrays = next_arrays
                
        return arrays[0]
        
    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array

if __name__ == "__main__":
    a = [[1,3,5,7],[2,4,6],[0,8,9,10,11]]
    print(Solution().mergeKSortedArrays(a))
    print(Solution().mergekKSortedArrays2(a))
    print(Solution().mergeKSortedArrays3(a))



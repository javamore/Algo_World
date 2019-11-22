""" 
lintcode 143
Given an array of n objects with k different colors (numbered from 1 to k), 
sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
You are not suppose to use the library's sort function for this problem.
k <= n

example1:
Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]

example2:
Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
#divide and conquer, using two zone, one is for color, another is to be sorted array zone
#find color zone middle, PARTITION, <= color go to left, > color go to right
#recursion, time: O(nlgk), n is total items, k is color kinds.

    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)


    def sort(self, colors, color_left, color_right, index_left, index_right):
        if color_left == color_right or index_left == index_right: 
            return
        
        # like mergesort,  //2.     
        color = (color_left + color_right) // 2
        
        #like quicksort, partition array.
        left, right = index_left, index_right
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                
        # color (color_left~color) in the zone index_left~right
        # color(color+1~ color_right) in the zone left~index_right
        self.sort(colors, color_left, color, index_left, right)
        self.sort(colors, color + 1, color_right, left, index_right)
        
        


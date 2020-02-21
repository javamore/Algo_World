"""
lintcode 35 Reverse Linked List
Example :

Input: 1->2->3->null
Output: 3->2->1->null

"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        cur, prev = head, None
        while cur:
            
            # record current node's next node
            tmp = cur.next
            
            # current node points to next node
            cur.next = prev
            
            # prev and cur both move forward one position
            prev = cur
            cur = tmp 
            
        return prev
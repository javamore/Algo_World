"""
lintcode 112
Remove duplicates from sorted list

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
	Input:  null
	Output: null

Example 2:
	Input:  1->1->2->null
	Output: 1->2->null

Example 3:
	Input:  1->1->2->3->3->null
	Output: 1->2->3->null
"""

#Definition of ListNode

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return head
        prev = head
        p = head.next
        
        while p:
            # if duplication appeared 
            if p.val == prev.val:
            #jump to neighbor element
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return head

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print (Solution().deleteDuplicates(head))

# time: O(n), space:O(1)

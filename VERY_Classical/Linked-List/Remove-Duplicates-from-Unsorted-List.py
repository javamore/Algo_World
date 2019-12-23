"""
lintcode 217
Write code to remove duplicates from an unsorted linked list.

Given a sorted linked list, delete all duplicates so that each element appear only once.

Example 1:
Input: 1->2->1->3->3->5->6->3->null
Output: 1->2->3->5->6->null

Example 2:
Input: 2->2->2->2->2->null
Output: 2->null
"""

#Definition of ListNode

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        maps = dict()
        if head == None or head.next == None:
            return head
        maps[head.val] = 1 
        p = head
        curr = head.next
        while curr :
            if curr.val not in maps:
                maps[curr.val] = 1
                p.next = curr
                p = p.next 
            curr = curr.next
        p.next = None
        return head
        

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print (Solution().removeDuplicates(head))

# time: O(n), space:O(1)

"""
__author__ = "rainbowbow "

    def removeDuplicates(self, head):
        # write your code here
        ele_set = set()
        if not head or not head.next:
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, cur = dummy, head
        
        while cur.next: #end: last element without check
            #check if val is in list, if so, then skip
            #if not then continue 
            if cur.val not in ele_set:
                ele_set.add(cur.val)
                pre = pre.next 
                cur = cur.next
            else:
                cur = cur.next
                pre.next = cur
                
        #handle last element ,check, no need to move next        
        if cur.val in ele_set:
            pre.next = None
        
        return dummy.next
"""

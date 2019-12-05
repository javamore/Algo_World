"""
lintcode 113
Remove duplicates from sorted list 2

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1
Input : 1->2->3->3->4->4->5->null
Output : 1->2->5->null

Example 2
Input : 1->1->1->2->3->null
Output : 2->3->null

"""

#dummy -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
#pre   cur

#make sure pre is always on ahead than cur.
# dummy[index] = -1
#   / 
# dummy -> 1 -> 2    3    3    4 -> 4 -> 5
#          |              |
#          ----------------
#       pre(dummy)            cur(head)

#check duplicates by cur.val == cur.next.val
#if duplicates exist, pre.next = cur.next; cur = cur.next
#if not exist, pre = cur; cur = cur.next

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
    
    def deleteDuplicates2(self, head):
        # write your code here
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head 

        while cur != None:
            duplicate = False
            # check whether has duplicates 
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
                duplicate = True
            
            if duplicate == False:
                pre = cur 
            else:
                pre.next = cur.next  

            cur = cur.next 
        return dummy.next

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print (Solution().deleteDuplicates2(head))

# time: O(n), space:O(1)

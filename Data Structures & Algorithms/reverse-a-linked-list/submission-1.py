# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is blank
        if not head:
            return 
        
        # set up 2 pointers
        prev = None
        curr = head
        
        # while current exists
        while curr:
            # set tmp to the next of current
            temp = curr.next
            # set current next to prev
            curr.next = prev
            # set prev to curr
            prev = curr
            # set curr to temp
            curr = temp
        
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = ListNode(0)
        dummy.next = head

        # to set up dual pointers
        fast = dummy
        slow = dummy

        # to create gap
        for _ in range(n):
            fast = fast.next
        
        # to get to end, slow = one to remove
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # skip the node 
        slow.next = slow.next.next

        return dummy.next
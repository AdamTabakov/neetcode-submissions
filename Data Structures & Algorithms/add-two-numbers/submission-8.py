# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        totals = ListNode()
        currT = totals
        carry = 0

        # while both exist
        while curr1 or curr2 or carry:
            
            # get the values for both
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            # set total
            total = val1 + val2 + carry

            # if needed to carry
            if total > 9:
                carry = 1
                total = total % 10
            else:
                carry = 0
            
            # add a new node to the linked list and proceed
            currT.next = ListNode(total)
            currT = currT.next

            # keep the other 2 linked lists going
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            
        return totals.next
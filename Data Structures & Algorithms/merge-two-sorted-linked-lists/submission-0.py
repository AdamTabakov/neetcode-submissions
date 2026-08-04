# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if either are none
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        # start will be a pointer towards starting, current will be a pointer that moves
        start = ListNode()
        current = start

        # while both lists exist
        while list1 and list2:
            # if the value of list1 is larger than the value of list2
            if list1.val < list2.val:
                # set the next node of current to list1
                current.next = list1
                # move list1 up to next
                list1 = list1.next
            # if the value of list2 is larger than the value of list1
            else:
                # set the next node of current to list2
                current.next = list2
                # move list2 up to next
                list2 = list2.next
            
            # move the current pointer up
            current = current.next
        # add the rest of either list1 or list2 to the current
        current.next = list1 or list2

        return start.next
        
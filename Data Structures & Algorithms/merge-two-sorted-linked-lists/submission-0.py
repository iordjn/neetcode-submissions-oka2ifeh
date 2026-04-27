# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        previous = dummy
        
        
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                previous.next = curr1
                previous = curr1
                curr1 = curr1.next
            else:
                previous.next = curr2
                previous = curr2
                curr2 = curr2.next

        while curr1 is not None:
            previous.next = curr1
            previous = curr1
            curr1 = curr1.next
        while curr2 is not None:
            previous.next = curr2
            previous = curr2
            curr2 = curr2.next
        
        return dummy.next
                
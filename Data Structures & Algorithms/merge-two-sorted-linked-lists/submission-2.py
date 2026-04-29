# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode(None)
        prev = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next

        while curr1 is not None:
            prev.next = curr1
            prev = curr1
            curr1 = curr1.next

        while curr2 is not None:
            prev.next = curr2
            prev = curr2
            curr2 = curr2.next

        return dummy.next

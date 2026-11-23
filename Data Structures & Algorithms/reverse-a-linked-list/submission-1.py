# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        
        current_node = head
        if current_node == None:
            return None
        next_node = head.next
        previous_node = None 
        
        while current_node is not None:

            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            if current_node == None:
                return previous_node
            next_node = current_node.next

        return current_node


                
            

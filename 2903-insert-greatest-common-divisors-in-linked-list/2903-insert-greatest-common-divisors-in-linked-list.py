# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers: 'prev_node' pointing to the current node being processed, 
        # and 'current_node' pointing to the next node in the list.
        prev_node, current_node = head, head.next
      
        # Iterate through the linked list until we reach the end.
        while current_node:
            # Compute Greatest Common Divisor (GCD) of the values in the 'prev_node' and 'current_node'.
            gcd_value = gcd(prev_node.val, current_node.val)
          
            # Insert a new node with the GCD value between the 'prev_node' and 'current_node'.
            prev_node.next = ListNode(gcd_value, current_node)
          
            # Update pointers: move 'prev_node' to the 'current_node' and
            # 'current_node' to the next node in the list.
            prev_node, current_node = current_node, current_node.next
      
        # Return the modified linked list head.
        return head
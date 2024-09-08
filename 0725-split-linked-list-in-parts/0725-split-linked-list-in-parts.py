# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_length, current_node = 0, root
        # Calculate the total length of the list
        while current_node:
            list_length += 1
            current_node = current_node.next
      
        
        current_node = root
        
        part_size, extra_nodes = divmod(list_length, k)
        
        result = [None for _ in range(k)]

        # Split the list into k parts
        for i in range(k):
            # The beginning of the current part
            part_head = current_node
            # Calculate the number of nodes this part should have
            current_part_size = part_size + (i < extra_nodes)

            # Iterate through the current part's nodes, stopping before the last node
            for j in range(current_part_size - 1):
                if current_node:
                    current_node = current_node.next
          
            # If there are nodes in the current part, disconnect this part from the next one
            if current_node:
                
                next_part = current_node.next
                
                current_node.next = None
           
                current_node = next_part
          
            # Update the result with the head of the current part
            result[i] = part_head
      
        return result
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, rows: int, cols: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * cols for _ in range(rows)]
      
        # The starting position (top-left corner)
        row, col = 0, 0
      
        # Direction indexes represent right, down, left, up movements
        direction = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
      
        # As long as the linked list has nodes
        while head:
            # Place the current node's value in the matrix
            matrix[row][col] = head.val
          
            # Move to the next node in the linked list
            head = head.next
          
            # Calculate the next position based on the current direction
            next_row, next_col = row + directions[direction][0], col + directions[direction][1]
          
            # Check if the next position is invalid or already filled
            if (next_row < 0 or next_col < 0 or 
                next_row >= rows or next_col >= cols or 
                matrix[next_row][next_col] != -1):
                # Change direction (right -> down -> left -> up -> right...)
                direction = (direction + 1) % 4
                next_row, next_col = row + directions[direction][0], col + directions[direction][1]

            # Update the current position to the next position
            row, col = next_row, next_col
      
        # Return the filled matrix
        return matrix

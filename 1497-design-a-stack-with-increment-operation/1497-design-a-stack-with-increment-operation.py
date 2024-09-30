class CustomStack:

    def __init__(self, max_size: int):
        # Initialize the stack with the given max size.
        # The actual stack is maintained in a list initialized with zeros.
        self.stack = [0] * max_size
        # The add list is used to store the additive increments for each position.
        self.add = [0] * max_size
        # The index `current_size` tracks the number of elements in the stack.
        self.current_size = 0

    def push(self, x: int) -> None:
        # Push an element onto the stack if there is space available.
        if self.current_size < len(self.stack):
            self.stack[self.current_size] = x
            self.current_size += 1


    def pop(self) -> int:
        # Pop the top element from the stack and apply any increments to it.
        if self.current_size <= 0:
            return -1  # Return -1 if the stack is empty.
        self.current_size -= 1
        result = self.stack[self.current_size] + self.add[self.current_size]
        # Transfer the increment to the next element to be popped, if applicable.
        if self.current_size > 0:
            self.add[self.current_size - 1] += self.add[self.current_size]
        # Reset the increment for the current position.
        self.add[self.current_size] = 0
        return result  # Return the final value after applying the increment.

    def increment(self, k: int, val: int) -> None:
        # Increment the bottom `k` elements of the stack by `val`.
        limit = min(k, self.current_size) - 1  # Determine the actual limit to increment.
        if limit >= 0:
            self.add[limit] += val  # Apply the increment to the `limit` position.


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
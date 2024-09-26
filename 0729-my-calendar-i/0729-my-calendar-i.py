from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.sorted_events = SortedDict()

    def book(self, start: int, end: int) -> bool:
        # Find the index of the first event that ends after the requested start time
        next_event_index = self.sorted_events.bisect_right(start)

        if next_event_index < len(self.sorted_events) and end > self.sorted_events.values()[next_event_index]:
            return False  # Event cannot be booked due to overlap

        # If there is no conflict, insert the new event into the sorted dictionary.
        self.sorted_events[end] = start
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
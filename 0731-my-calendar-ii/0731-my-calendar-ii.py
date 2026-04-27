class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start, end):
        for s, e in self.overlaps:
            if max(s, start) < min(e, end):
                return False
        
        for s, e in self.booked:
            if max(s, start) < min(e, end):
                self.overlaps.append((max(s, start), min(e, end)))
        
        self.booked.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
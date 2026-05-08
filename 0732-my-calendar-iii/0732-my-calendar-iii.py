from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.mp = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.mp[startTime] = self.mp.get(startTime,0)+1
        self.mp[endTime] = self.mp.get(endTime,0)-1

        cur = ans = 0
        for v in self.mp.values():
            cur += v
            ans = max(ans, cur)

        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
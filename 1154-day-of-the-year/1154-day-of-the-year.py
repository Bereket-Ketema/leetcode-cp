class Solution:
    def dayOfYear(self, date):
        y, m, d = map(int, date.split('-'))

        days = [31,28,31,30,31,30,31,31,30,31,30,31]

        leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
        if leap:
            days[1] = 29

        return sum(days[:m-1]) + d
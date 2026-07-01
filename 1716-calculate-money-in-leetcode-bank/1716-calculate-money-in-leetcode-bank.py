class Solution:
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7
        
        ans = weeks * 28 + 7 * weeks * (weeks - 1) // 2
        
        start = weeks + 1
        for i in range(days):
            ans += start + i
        
        return ans
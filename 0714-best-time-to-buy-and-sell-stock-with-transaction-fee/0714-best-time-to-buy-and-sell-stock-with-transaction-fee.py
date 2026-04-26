class Solution:
    def maxProfit(self, prices, fee):
        hold = -prices[0]
        cash = 0
        
        for p in prices[1:]:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        
        return cash
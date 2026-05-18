class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        ans = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new = empty // numExchange
            ans += new
            empty = new + empty % numExchange
        
        return ans
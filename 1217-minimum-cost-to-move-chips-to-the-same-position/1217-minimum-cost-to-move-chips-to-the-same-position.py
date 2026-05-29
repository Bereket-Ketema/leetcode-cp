class Solution:
    def minCostToMoveChips(self, position):
        odd = even = 0
        
        for x in position:
            if x % 2:
                odd += 1
            else:
                even += 1
        
        return min(odd, even)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        indx = len(piles)//3
        count = 0
        for i in range(indx,len(piles),2):
            count += piles[i]
        return count

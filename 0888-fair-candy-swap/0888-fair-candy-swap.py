class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        s = set(bobSizes)
        
        for x in aliceSizes:
            if x-diff in s:
                return [x, x-diff]
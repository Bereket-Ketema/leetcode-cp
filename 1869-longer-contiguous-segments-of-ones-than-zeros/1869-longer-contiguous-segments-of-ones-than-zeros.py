class Solution:
    def checkZeroOnes(self, s):
        max1 = max0 = cur1 = cur0 = 0
        
        for ch in s:
            if ch == '1':
                cur1 += 1
                cur0 = 0
            else:
                cur0 += 1
                cur1 = 0
            
            max1 = max(max1, cur1)
            max0 = max(max0, cur0)
        
        return max1 > max0
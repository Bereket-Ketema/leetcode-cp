class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9
        
        upper = 10**n - 1
        lower = 10**(n-1)
        
        for left in range(upper, lower-1, -1):
            p = int(str(left) + str(left)[::-1])
            for x in range(upper, lower-1, -1):
                if p // x > upper:
                    break
                if x * (p // x) == p:
                    return p % 1337
class Solution:
    def getNoZeroIntegers(self, n):
        def ok(x):
            return '0' not in str(x)
        
        for a in range(1, n):
            b = n - a
            if ok(a) and ok(b):
                return [a, b]
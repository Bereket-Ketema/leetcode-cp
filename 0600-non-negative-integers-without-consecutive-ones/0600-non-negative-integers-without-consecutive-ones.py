class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1, 2]
        for _ in range(2, 32):
            fib.append(fib[-1] + fib[-2])
        
        prev_bit = 0
        res = 0
        
        for i in range(30, -1, -1):
            if n & (1 << i):
                res += fib[i]
                if prev_bit == 1:
                    return res
                prev_bit = 1
            else:
                prev_bit = 0
        
        return res + 1
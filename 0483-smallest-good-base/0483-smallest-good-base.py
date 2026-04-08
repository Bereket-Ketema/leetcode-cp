class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = n.bit_length()
        
        for m in range(max_m, 1, -1):
            k = int(n ** (1/(m-1)))
            if k > 1:
                s = 1
                curr = 1
                for _ in range(m-1):
                    curr *= k
                    s += curr
                if s == n:
                    return str(k)
        
        return str(n-1)
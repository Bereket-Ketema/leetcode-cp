class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        m = bin(x)[2:]
        n = bin(y)[2:]
        
        if len(n) > len(m):
            r = len(n) - len(m)
            m = m.zfill(len(m) + r)
        elif len(m) > len(n):
            r = len(m) - len(n)
            n = n.zfill(len(n) + r)
        
        left, right = 0, 0
        ans = 0
        while right < len(n):
            if m[left] != n[right]:
                ans += 1
            left += 1
            right += 1

        return ans
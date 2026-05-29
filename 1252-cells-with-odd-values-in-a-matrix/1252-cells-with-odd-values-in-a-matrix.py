class Solution:
    def oddCells(self, m, n, indices):
        rows = [0] * m
        cols = [0] * n
        
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if rows[i] ^ cols[j]:
                    ans += 1
        
        return ans
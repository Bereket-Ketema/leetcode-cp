class Solution:
    def minDeletionSize(self, strs):
        m,n = len(strs), len(strs[0])
        ans = 0
        
        for c in range(n):
            for r in range(1,m):
                if strs[r][c] < strs[r-1][c]:
                    ans += 1
                    break
        
        return ans
class Solution:
    def checkPartitioning(self, s):
        n = len(s)
        
        pal = [[False]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i < 2 or pal[i+1][j-1]):
                    pal[i][j] = True
        
        for i in range(n-2):
            for j in range(i+1,n-1):
                if pal[0][i] and pal[i+1][j] and pal[j+1][n-1]:
                    return True
        
        return False
class Solution:
    def tilingRectangle(self, n, m):
        if n > m:
            n,m = m,n
        
        self.ans = n*m
        height = [0]*m
        
        def dfs(cnt):
            if cnt >= self.ans:
                return
            
            min_h = min(height)
            if min_h == n:
                self.ans = min(self.ans,cnt)
                return
            
            idx = height.index(min_h)
            end = idx
            
            while end<m and height[end]==min_h and end-idx+1<=n-min_h:
                end+=1
            
            for j in range(end-1,idx-1,-1):
                size=j-idx+1
                
                for k in range(idx,j+1):
                    height[k]+=size
                
                dfs(cnt+1)
                
                for k in range(idx,j+1):
                    height[k]-=size
        
        dfs(0)
        return self.ans
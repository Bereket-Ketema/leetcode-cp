from collections import Counter

class Solution:
    def gridIllumination(self, n, lamps, queries):
        rows = Counter()
        cols = Counter()
        diag = Counter()
        anti = Counter()
        
        active = set()
        
        for x,y in lamps:
            if (x,y) in active:
                continue
            
            active.add((x,y))
            rows[x] += 1
            cols[y] += 1
            diag[x-y] += 1
            anti[x+y] += 1
        
        ans = []
        
        for x,y in queries:
            if (rows[x] or cols[y] or
                diag[x-y] or anti[x+y]):
                ans.append(1)
            else:
                ans.append(0)
            
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    nx,ny = x+dx,y+dy
                    
                    if (nx,ny) in active:
                        active.remove((nx,ny))
                        
                        rows[nx] -= 1
                        cols[ny] -= 1
                        diag[nx-ny] -= 1
                        anti[nx+ny] -= 1
        
        return ans
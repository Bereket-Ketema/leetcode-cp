import math

class Solution:
    def numPoints(self, darts, r):
        n=len(darts)
        ans=1
        
        for i in range(n):
            for j in range(i+1,n):
                x1,y1=darts[i]
                x2,y2=darts[j]
                d=math.dist((x1,y1),(x2,y2))
                if d>2*r:
                    continue
                
                mx=(x1+x2)/2
                my=(y1+y2)/2
                h=(r*r-(d/2)**2)**0.5
                
                dx=(y1-y2)/d
                dy=(x2-x1)/d
                
                for sx,sy in [(mx+dx*h,my+dy*h),(mx-dx*h,my-dy*h)]:
                    cnt=0
                    for x,y in darts:
                        if (x-sx)**2+(y-sy)**2<=r*r+1e-7:
                            cnt+=1
                    ans=max(ans,cnt)
        return ans
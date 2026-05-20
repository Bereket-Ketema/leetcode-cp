import math

class Solution:
    def visiblePoints(self, points, angle, location):
        same = 0
        arr = []
        
        x0,y0 = location
        
        for x,y in points:
            if [x,y] == location:
                same += 1
            else:
                arr.append(math.degrees(math.atan2(y-y0,x-x0)))
        
        arr.sort()
        arr += [x+360 for x in arr]
        
        ans = l = 0
        
        for r in range(len(arr)):
            while arr[r]-arr[l] > angle:
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans + same
class Solution:
    def countGoodRectangles(self, rectangles):
        mx = 0
        cnt = 0
        
        for l,w in rectangles:
            side = min(l,w)
            
            if side > mx:
                mx = side
                cnt = 1
            elif side == mx:
                cnt += 1
        
        return cnt
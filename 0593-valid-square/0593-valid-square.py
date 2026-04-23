class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def dist(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        
        points = [p1, p2, p3, p4]
        dists = sorted(dist(points[i], points[j]) 
                       for i in range(4) for j in range(i+1, 4))
        
        return dists[0] > 0 and \
               dists[0] == dists[1] == dists[2] == dists[3] and \
               dists[4] == dists[5]
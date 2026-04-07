class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        
        for i in range(len(points)):
            dist_map = defaultdict(int)
            for j in range(len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = dx*dx + dy*dy
                dist_map[dist] += 1
            
            for val in dist_map.values():
                res += val * (val - 1)
        
        return res
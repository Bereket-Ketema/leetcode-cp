class Solution:
    def leastBricks(self, wall):
        from collections import Counter
        count = Counter()
        
        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                count[pos] += 1
        
        return len(wall) - (max(count.values()) if count else 0)
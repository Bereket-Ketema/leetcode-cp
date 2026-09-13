class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a_ones = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        b_ones = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        counts = collections.Counter()
        max_overlaps = 0
        
        for r1, c1 in a_ones:
            for r2, c2 in b_ones:
                shift = (r2 - r1, c2 - c1)
                counts[shift] += 1
                max_overlaps = max(max_overlaps, counts[shift])
                
        return max_overlaps
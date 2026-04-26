class Solution:
    def largestOverlap(self, img1, img2):
        from collections import Counter
        
        A = [(i, j) for i in range(len(img1)) for j in range(len(img1)) if img1[i][j]]
        B = [(i, j) for i in range(len(img2)) for j in range(len(img2)) if img2[i][j]]
        
        count = Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
        return max(count.values() or [0])
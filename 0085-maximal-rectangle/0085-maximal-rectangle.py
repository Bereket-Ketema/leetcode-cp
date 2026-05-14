class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        
        def largestRectangleArea(h):
            stack = []
            res = 0
            h.append(0)
            
            for i, x in enumerate(h):
                while stack and h[stack[-1]] > x:
                    height = h[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(i)
            
            h.pop()
            return res
        
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            ans = max(ans, largestRectangleArea(heights))
        
        return ans
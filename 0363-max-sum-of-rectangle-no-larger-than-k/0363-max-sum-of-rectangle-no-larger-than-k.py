import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        
        for left in range(n):
            row_sum = [0] * m
            
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                
                prefix = [0]
                cur = 0
                
                for s in row_sum:
                    cur += s
                    idx = bisect.bisect_left(prefix, cur-k)
                    if idx < len(prefix):
                        ans = max(ans, cur-prefix[idx])
                    bisect.insort(prefix, cur)
        
        return ans
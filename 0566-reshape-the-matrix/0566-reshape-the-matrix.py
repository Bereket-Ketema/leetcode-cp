class Solution:
    def matrixReshape(self, mat, r, c):
        flat = []
        
        for row in mat:
            flat.extend(row)
        
        if len(flat) != r * c:
            return mat
        
        ans = []
        
        for i in range(0, len(flat), c):
            ans.append(flat[i:i+c])
        
        return ans
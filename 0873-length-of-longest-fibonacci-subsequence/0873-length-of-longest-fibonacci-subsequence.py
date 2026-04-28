class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = {}
        res = 0
        
        for j in range(n):
            for i in range(j):
                k = arr[j] - arr[i]
                if k < arr[i] and k in index:
                    prev = index[k]
                    dp[(i, j)] = dp.get((prev, i), 2) + 1
                    res = max(res, dp[(i, j)])
        
        return res if res >= 3 else 0
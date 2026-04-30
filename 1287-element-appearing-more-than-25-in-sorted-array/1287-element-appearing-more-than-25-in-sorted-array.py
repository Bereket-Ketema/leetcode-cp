class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr)
        for i in [n//4, n//2, 3*n//4]:
            if arr.count(arr[i]) > n // 4:
                return arr[i]
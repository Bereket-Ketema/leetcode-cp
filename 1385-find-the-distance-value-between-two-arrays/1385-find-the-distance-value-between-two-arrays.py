class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        res = 0
        for a in arr1:
            if all(abs(a - b) > d for b in arr2):
                res += 1
        return res
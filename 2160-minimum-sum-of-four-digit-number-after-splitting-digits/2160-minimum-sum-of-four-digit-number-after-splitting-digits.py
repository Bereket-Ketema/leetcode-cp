class Solution:
    def minimumSum(self, num):
        d = sorted(str(num))

        return int(d[0] + d[2]) + int(d[1] + d[3])
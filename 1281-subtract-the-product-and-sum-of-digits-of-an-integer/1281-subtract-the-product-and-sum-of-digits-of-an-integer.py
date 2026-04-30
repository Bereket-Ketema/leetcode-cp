class Solution:
    def subtractProductAndSum(self, n):
        prod, s = 1, 0
        for d in str(n):
            prod *= int(d)
            s += int(d)
        return prod - s
import math

class Solution:
    def isGoodArray(self, nums):
        g = nums[0]

        for x in nums:
            g = math.gcd(g,x)

        return g == 1
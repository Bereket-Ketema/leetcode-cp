class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        mx = max(candies)
        return [x + extraCandies >= mx for x in candies]
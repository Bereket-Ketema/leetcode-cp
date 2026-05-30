class Solution:
    def countElements(self, nums):
        mn = min(nums)
        mx = max(nums)

        return sum(mn < x < mx for x in nums)
class Solution:
    def arithmeticTriplets(self, nums, diff):
        s = set(nums)
        ans = 0

        for x in nums:
            if x + diff in s and x + 2 * diff in s:
                ans += 1

        return ans
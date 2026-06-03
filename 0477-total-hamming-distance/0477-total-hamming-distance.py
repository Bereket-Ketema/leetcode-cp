class Solution:
    def totalHammingDistance(self, nums):
        n = len(nums)
        ans = 0

        for bit in range(32):
            ones = 0

            for num in nums:
                if (num >> bit) & 1:
                    ones += 1

            ans += ones * (n - ones)

        return ans
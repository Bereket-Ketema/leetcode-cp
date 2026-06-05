class Solution:
    def frequencySort(self, nums):
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        return sorted(nums, key=lambda x: (freq[x], -x))
class Solution:
    def singleNumber(self, nums):
        freq = Counter(nums)
        for k, v in freq.items():
            if v == 1:
                return k
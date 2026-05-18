class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)

        add = 0
        for k, v in freq.items():
            if v == 1:
                add += k
        
        return add
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        pair = 0
        alone = 0

        for v in frequency.values():
            if v % 2 == 0:
                pair += v // 2
            elif v > 1:
                pair += (v - 1) // 2
                alone += 1
            else:
                alone += 1
        
        return [pair, alone]
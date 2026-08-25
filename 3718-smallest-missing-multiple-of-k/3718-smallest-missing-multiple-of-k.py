class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        store = set(nums)
        n = 1
        
        while True:
            if n % k == 0 and n not in store:
                return n
            
            n += 1


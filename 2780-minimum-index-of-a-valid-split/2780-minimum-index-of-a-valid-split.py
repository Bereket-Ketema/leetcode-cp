class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        key = max(freq, key=freq.get)

        if freq[key] * 2 <= len(nums):
            return -1
        
        left = 0
        total = freq[key]

        for i in range(len(nums)-1):
            if nums[i] == key:
                left += 1
            
            right = total - left

            if left * 2 > (i+1) and right * 2 > (len(nums)-i-1):
                return i

        return -1

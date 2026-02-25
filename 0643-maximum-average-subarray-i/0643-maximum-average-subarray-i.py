class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window_sum = 0
        window = sum(nums[:k])
        window_sum = window

        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i-k]
            window_sum = max(window_sum, window)
        
        return window_sum / k

        
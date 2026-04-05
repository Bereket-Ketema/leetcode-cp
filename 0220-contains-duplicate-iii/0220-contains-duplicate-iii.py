import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0 or t < 0:
            return False
        
        window = []
        
        for i, num in enumerate(nums):
            pos = bisect.bisect_left(window, num - t)
            
            if pos < len(window) and abs(window[pos] - num) <= t:
                return True
            
            bisect.insort(window, num)
            
            if len(window) > k:
                remove_pos = bisect.bisect_left(window, nums[i - k])
                window.pop(remove_pos)
        
        return False
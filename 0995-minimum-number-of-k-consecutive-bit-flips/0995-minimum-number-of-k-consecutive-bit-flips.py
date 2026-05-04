from collections import deque

class Solution:
    def minKBitFlips(self, nums, k):
        q = deque()
        flips = 0
        
        for i in range(len(nums)):
            if q and q[0] == i:
                q.popleft()
            
            cur = len(q) % 2
            
            if nums[i] == cur:
                if i + k > len(nums):
                    return -1
                flips += 1
                q.append(i+k)
        
        return flips
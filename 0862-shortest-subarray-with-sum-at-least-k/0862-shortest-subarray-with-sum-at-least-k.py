from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0]
        
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        dq = deque()
        ans = float('inf')
        
        for i in range(n+1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return ans if ans != float('inf') else -1
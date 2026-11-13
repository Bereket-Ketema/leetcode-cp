from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        curr_cost = 0
        right = n - 1
        ans = 0
        
        for left in range(n - 1, -1, -1):
            val = nums[left]
            count = 1
            
            while dq and dq[0][0] < val:
                block_val, block_cnt = dq.popleft()
                curr_cost += (val - block_val) * block_cnt
                count += block_cnt
                
            dq.appendleft((val, count))
            
            while curr_cost > k:
                block_val, block_cnt = dq.pop()
                curr_cost -= (block_val - nums[right])
                if block_cnt > 1:
                    dq.append((block_val, block_cnt - 1))
                right -= 1
                
            ans += right - left + 1
            
        return ans
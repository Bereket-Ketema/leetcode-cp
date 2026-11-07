import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # available: min-heap of (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        
        # busy: min-heap of (release_time, weight, index)
        busy = []
        
        ans = []
        current_time = 0
        
        for i, task_time in enumerate(tasks):
            current_time = max(current_time, i)
            
            # Free up servers whose tasks have finished by current_time
            while busy and busy[0][0] <= current_time:
                _, weight, s_idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, s_idx))
                
            # If no servers are available, jump forward in time to the earliest completion
            if not available:
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    _, weight, s_idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, s_idx))
                    
            weight, s_idx = heapq.heappop(available)
            ans.append(s_idx)
            heapq.heappush(busy, (current_time + task_time, weight, s_idx))
            
        return ans
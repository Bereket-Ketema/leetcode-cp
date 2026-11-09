import bisect
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        count = [0] * k
        busy = []  # min-heap storing (free_time, server_id)
        available = list(range(k))  # sorted list of available server IDs
        
        for i, (t, d) in enumerate(zip(arrival, load)):
            # Free up servers that have finished before or at current arrival time t
            while busy and busy[0][0] <= t:
                _, server_id = heapq.heappop(busy)
                bisect.insort(available, server_id)
                
            if not available:
                continue
                
            target = i % k
            # Find the smallest server_id >= target
            idx = bisect.bisect_left(available, target)
            
            # If no available server >= target, wrap around to the first available server
            if idx == len(available):
                idx = 0
                
            server_id = available.pop(idx)
            count[server_id] += 1
            heapq.heappush(busy, (t + d, server_id))
            
        max_req = max(count)
        return [i for i, c in enumerate(count) if c == max_req]
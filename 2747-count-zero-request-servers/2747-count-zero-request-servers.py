from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time: logs[i] = [server_id, time]
        logs.sort(key=lambda item: item[1])
        
        # Sort queries while keeping track of their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        active_counts = defaultdict(int)
        distinct_active = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q_time in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand the right side of the window (add logs where time <= window_end)
            while right < num_logs and logs[right][1] <= window_end:
                server = logs[right][0]
                if active_counts[server] == 0:
                    distinct_active += 1
                active_counts[server] += 1
                right += 1
                
            # Shrink the left side of the window (remove logs where time < window_start)
            while left < num_logs and logs[left][1] < window_start:
                server = logs[left][0]
                active_counts[server] -= 1
                if active_counts[server] == 0:
                    distinct_active -= 1
                left += 1
                
            ans[orig_idx] = n - distinct_active
            
        return ans
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        
        prev = (0, "")
        result = []
        
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)
            
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            
            prev = (freq + 1, char)
        
        res = "".join(result)
        return res if len(res) == len(s) else ""
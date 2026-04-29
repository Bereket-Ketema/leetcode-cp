import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(w/q, q) for q, w in zip(quality, wage)])
        
        heap = []
        total_q = 0
        res = float('inf')
        
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_q += q
            
            if len(heap) > k:
                total_q += heapq.heappop(heap)
            
            if len(heap) == k:
                res = min(res, total_q * ratio)
        
        return res
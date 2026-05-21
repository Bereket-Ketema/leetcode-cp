import heapq

class Solution:
    def kthSmallest(self, mat, k):
        cur = [0]
        
        for row in mat:
            heap = []
            
            for x in cur:
                for y in row:
                    heapq.heappush(heap, x+y)
            
            cur = []
            for _ in range(min(k, len(heap))):
                cur.append(heapq.heappop(heap))
        
        return cur[k-1]
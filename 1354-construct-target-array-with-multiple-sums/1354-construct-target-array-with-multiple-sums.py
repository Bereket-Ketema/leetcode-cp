import heapq

class Solution:
    def isPossible(self, target):
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        
        while True:
            x = -heapq.heappop(heap)
            rest = total - x
            
            if x == 1 or rest == 1:
                return True
            if rest == 0 or x < rest or x % rest == 0:
                return False
            
            new = x % rest
            total = rest + new
            heapq.heappush(heap, -new)
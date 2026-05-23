import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        heap = []
        fuel = startFuel
        i = 0
        ans = 0
        
        while fuel < target:
            while i < len(stations) and stations[i][0] <= fuel:
                heapq.heappush(heap, -stations[i][1])
                i += 1
            
            if not heap:
                return -1
            
            fuel += -heapq.heappop(heap)
            ans += 1
        
        return ans
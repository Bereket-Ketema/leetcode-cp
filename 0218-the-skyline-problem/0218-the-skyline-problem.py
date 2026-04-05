import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for L, R, H in buildings:
            events.append((L, -H)) 
            events.append((R, H))  

        events.sort(key=lambda x: (x[0], x[1]))

        result = []
        heap = [0] 
        prev_max = 0
        import collections
        counter = collections.Counter({0:1}) 

        for x, h in events:
            if h < 0: 
                counter[-h] += 1
                heapq.heappush(heap, h)
            else:  
                counter[h] -= 1
                if counter[h] == 0:
                    del counter[h]

            while heap and -heap[0] not in counter:
                heapq.heappop(heap)

            curr_max = -heap[0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result
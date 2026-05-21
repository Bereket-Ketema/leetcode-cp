from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        have = set(initialBoxes)
        q = deque(initialBoxes)
        used = set()
        ans = 0
        
        while q:
            box = q.popleft()
            
            if box in used or status[box] == 0:
                continue
            
            used.add(box)
            ans += candies[box]
            
            for k in keys[box]:
                status[k] = 1
                if k in have:
                    q.append(k)
            
            for b in containedBoxes[box]:
                have.add(b)
                q.append(b)
        
        return ans
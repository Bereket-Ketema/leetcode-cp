from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        r = deque()
        d = deque()
        n = len(senate)
        
        for i, ch in enumerate(senate):
            if ch == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            if r[0] < d[0]:
                r.append(r.popleft() + n)
                d.popleft()
            else:
                d.append(d.popleft() + n)
                r.popleft()
        
        return "Radiant" if r else "Dire"
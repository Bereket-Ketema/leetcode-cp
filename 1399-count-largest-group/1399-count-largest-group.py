from collections import defaultdict

class Solution:
    def countLargestGroup(self, n):
        mp = defaultdict(int)
        
        for i in range(1, n+1):
            s = sum(map(int, str(i)))
            mp[s] += 1
        
        mx = max(mp.values())
        return sum(v == mx for v in mp.values())
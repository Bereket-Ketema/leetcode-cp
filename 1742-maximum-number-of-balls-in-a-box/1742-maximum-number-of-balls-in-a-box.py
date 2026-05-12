from collections import defaultdict

class Solution:
    def countBalls(self, lowLimit, highLimit):
        mp = defaultdict(int)

        for num in range(lowLimit, highLimit + 1):
            s = sum(map(int, str(num)))
            mp[s] += 1

        return max(mp.values())
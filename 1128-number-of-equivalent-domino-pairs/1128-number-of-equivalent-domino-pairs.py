from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes):
        cnt = Counter(tuple(sorted(d)) for d in dominoes)
        ans = 0
        
        for v in cnt.values():
            ans += v*(v-1)//2
        
        return ans
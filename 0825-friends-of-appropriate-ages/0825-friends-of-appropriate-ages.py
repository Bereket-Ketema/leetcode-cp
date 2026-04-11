class Solution:
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        res = 0
        
        for a in range(1, 121):
            if count[a] == 0:
                continue
            for b in range(1, 121):
                if count[b] == 0:
                    continue
                
                if b <= 0.5 * a + 7:
                    continue
                if b > a:
                    continue
                if b > 100 and a < 100:
                    continue
                
                res += count[a] * (count[b] - (a == b))
        
        return res
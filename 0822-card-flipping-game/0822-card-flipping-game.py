class Solution:
    def flipgame(self, fronts, backs):
        same = {x for x,y in zip(fronts,backs) if x==y}
        
        ans = float('inf')
        
        for x in fronts+backs:
            if x not in same:
                ans = min(ans,x)
        
        return 0 if ans==float('inf') else ans
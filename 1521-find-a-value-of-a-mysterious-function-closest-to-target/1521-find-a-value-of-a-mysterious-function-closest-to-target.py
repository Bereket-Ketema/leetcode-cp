class Solution:
    def closestToTarget(self, arr, target):
        ans=float('inf')
        prev=set()
        
        for x in arr:
            cur={x}
            for v in prev:
                cur.add(v&x)
            prev=cur
            
            for v in cur:
                ans=min(ans,abs(v-target))
        
        return ans
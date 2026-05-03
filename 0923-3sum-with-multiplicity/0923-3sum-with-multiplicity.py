from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9+7
        c = Counter(arr)
        nums = sorted(c)
        ans = 0
        
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[i:],i):
                z = target-x-y
                if z < y or z not in c:
                    continue
                
                if x==y==z:
                    ans += c[x]*(c[x]-1)*(c[x]-2)//6
                elif x==y:
                    ans += c[x]*(c[x]-1)//2*c[z]
                elif y==z:
                    ans += c[y]*(c[y]-1)//2*c[x]
                else:
                    ans += c[x]*c[y]*c[z]
        
        return ans%MOD
class Solution:
    def longestDupSubstring(self, s):
        nums=[ord(c)-97 for c in s]
        mod=(1<<61)-1
        n=len(s)
        
        def check(L):
            h=0
            base=26
            power=pow(base,L,mod)
            seen=set()
            
            for i in range(n):
                h=(h*base+nums[i])%mod
                if i>=L:
                    h=(h-power*nums[i-L])%mod
                
                if i>=L-1:
                    if h in seen:
                        return i-L+1
                    seen.add(h)
            return -1
        
        l,r=1,n
        ans=""
        
        while l<=r:
            m=(l+r)//2
            idx=check(m)
            if idx!=-1:
                ans=s[idx:idx+m]
                l=m+1
            else:
                r=m-1
        
        return ans
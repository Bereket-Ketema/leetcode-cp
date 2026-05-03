class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n=len(arr)
        l=0
        
        while l+1<n and arr[l]<=arr[l+1]:
            l+=1
        
        if l==n-1:
            return 0
        
        r=n-1
        while r>0 and arr[r-1]<=arr[r]:
            r-=1
        
        ans=min(n-l-1,r)
        i=0
        
        while i<=l and r<n:
            if arr[i]<=arr[r]:
                ans=min(ans,r-i-1)
                i+=1
            else:
                r+=1
        
        return ans
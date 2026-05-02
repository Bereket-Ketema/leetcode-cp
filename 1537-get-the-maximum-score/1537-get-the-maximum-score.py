class Solution:
    def maxSum(self, nums1, nums2):
        i=j=0
        s1=s2=0
        MOD=10**9+7
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                s1+=nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                s2+=nums2[j]
                j+=1
            else:
                s=max(s1,s2)+nums1[i]
                s1=s2=s
                i+=1
                j+=1
        
        s1+=sum(nums1[i:])
        s2+=sum(nums2[j:])
        return max(s1,s2)%MOD
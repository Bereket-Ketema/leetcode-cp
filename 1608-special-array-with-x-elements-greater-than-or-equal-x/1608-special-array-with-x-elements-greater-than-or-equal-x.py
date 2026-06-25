class Solution:
    def specialArray(self, nums):
        nums.sort()
        n = len(nums)
        
        for x in range(n + 1):
            cnt = sum(num >= x for num in nums)
            
            if cnt == x:
                return x
        
        return -1
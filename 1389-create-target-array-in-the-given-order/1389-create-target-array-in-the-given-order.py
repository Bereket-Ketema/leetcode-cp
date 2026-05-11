class Solution:
    def createTargetArray(self, nums, index):
        res = []
        
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        
        return res
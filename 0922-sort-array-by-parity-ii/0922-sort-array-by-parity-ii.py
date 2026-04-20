class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
        new = []
        for i in range(len(even)):
            new.append(even[i])
            new.append(odd[i])
        
        return new

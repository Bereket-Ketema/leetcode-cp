class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        inc, dec = 0, 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc += 1

            if nums[i] < nums[i - 1]:
                dec += 1
                
            if inc > 0 and dec > 0:
                return False

        return True
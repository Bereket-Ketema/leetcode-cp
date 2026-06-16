class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            work = nums.copy()
            work.pop(i)

            l, r = 0, 1
            flag = True

            while r < len(work):
                if work[l] >= work[r]:
                    flag = False
                    break
                
                l += 1
                r += 1
            
            if flag:
                return True
        
        return False


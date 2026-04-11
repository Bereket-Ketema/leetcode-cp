import random

class Solution:
    def findKthLargest(self, nums, k):
        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]
            p, i, j = l, l, r
            
            while i <= j:
                if nums[i] > pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1
            
            if k - 1 < p:
                return quickselect(l, p - 1)
            elif k - 1 > j:
                return quickselect(j + 1, r)
            else:
                return nums[k - 1]
        
        return quickselect(0, len(nums) - 1)
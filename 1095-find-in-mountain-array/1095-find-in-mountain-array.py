# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target, mountain_arr):
        def find_peak():
            l, r = 0, mountain_arr.length() - 1
            while l < r:
                m = (l + r) // 2
                if mountain_arr.get(m) < mountain_arr.get(m + 1):
                    l = m + 1
                else:
                    r = m
            return l
        
        def binary_search(l, r, target, asc=True):
            while l <= r:
                m = (l + r) // 2
                val = mountain_arr.get(m)
                
                if val == target:
                    return m
                
                if asc:
                    if val < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if val > target:
                        l = m + 1
                    else:
                        r = m - 1
            return -1
        
        peak = find_peak()
        
        left = binary_search(0, peak, target, True)
        if left != -1:
            return left
        
        return binary_search(peak + 1, mountain_arr.length() - 1, target, False)
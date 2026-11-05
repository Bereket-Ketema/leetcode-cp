import bisect
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for num in arr1:
            # Find the position where num would fit in sorted arr2
            idx = bisect.bisect_left(arr2, num)
            
            # Check the element at idx (if it exists)
            has_close = False
            if idx < len(arr2) and abs(arr2[idx] - num) <= d:
                has_close = True
            
            # Check the element to the left of idx (if it exists)
            if idx > 0 and abs(arr2[idx - 1] - num) <= d:
                has_close = True
                
            if not has_close:
                count += 1
                
        return count
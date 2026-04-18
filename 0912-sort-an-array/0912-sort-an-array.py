class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def divide(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2

            left_side = divide(arr[:mid])
            right_side = divide(arr[mid:])

            return combine(left_side, right_side)
        
        def combine(left_side, right_side):
            ans = []
            ptr1, ptr2 = 0, 0
            while ptr1 < len(left_side) and ptr2 < len(right_side):
                if left_side[ptr1] > right_side[ptr2]:
                    ans.append(right_side[ptr2])
                    ptr2 += 1
                else:
                    ans.append(left_side[ptr1])
                    ptr1 += 1

            ans.extend(left_side[ptr1:])
            ans.extend(right_side[ptr2:])

            return ans
        
        return divide(nums)


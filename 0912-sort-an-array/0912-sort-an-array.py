class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def divide(left, right, arr):
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            left_side = divide(left, mid, arr)
            right_side = divide(mid + 1, right, arr)

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
        
        return divide(0, len(nums) - 1, nums)


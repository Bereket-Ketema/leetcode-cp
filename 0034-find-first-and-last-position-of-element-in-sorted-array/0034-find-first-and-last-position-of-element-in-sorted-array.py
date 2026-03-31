class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_pos(nums, target, starting):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    if starting:
                        right = mid -1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        return [ get_pos(nums, target, True), get_pos(nums, target, False) ]
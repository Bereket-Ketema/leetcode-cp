class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        def binary(targ, find):
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == targ:
                    res = mid
                    if find:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < targ:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        left = binary(target, True)
        if left == -1:
            return []
        right = binary(target, False)
        return list(range(left, right + 1))
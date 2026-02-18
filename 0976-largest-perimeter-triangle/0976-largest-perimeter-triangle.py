class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        final = 0
        for i in range(len(nums)-2):
            case1 = nums[i] + nums[i+1] > nums[i+2]
            case2 = nums[i] + nums[i+2] > nums[i+1]
            case3 = nums[i+1] + nums[i+2] > nums[i]
            if case1 and case2 and case3:
                final = max(final,nums[i]+ nums[i+1] + nums[i+2])
        return final
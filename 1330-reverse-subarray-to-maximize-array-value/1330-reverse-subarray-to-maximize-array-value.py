class Solution:
    def maxValueAfterReverse(self, nums):
        total = 0

        for i in range(len(nums)-1):
            total += abs(nums[i]-nums[i+1])

        gain = 0
        low = float('inf')
        high = float('-inf')

        for i in range(len(nums)-1):
            a,b = nums[i], nums[i+1]

            gain = max(gain,
                abs(nums[0]-b)-abs(a-b),
                abs(nums[-1]-a)-abs(a-b)
            )

            low = min(low, max(a,b))
            high = max(high, min(a,b))

        return total + max(gain, 2*(high-low))
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = nums
        self.prev = nums[0]

        for i in range(1,len(nums)):
            self.prefix_sum[i] = self.prev + nums[i]
            self.prev = self.prefix_sum[i]

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] -self.prefix_sum[left-1]
        
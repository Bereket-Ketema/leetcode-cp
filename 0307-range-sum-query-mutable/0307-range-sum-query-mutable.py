class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        pos = index + self.n
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]

    def sumRange(self, left, right):
        left += self.n
        right += self.n
        s = 0
        while left <= right:
            if left % 2 == 1:
                s += self.tree[left]
                left += 1
            if right % 2 == 0:
                s += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return s
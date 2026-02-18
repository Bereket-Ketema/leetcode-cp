class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        store = []

        for i in range(size):
            count = 0
            for j in range(size):
                if nums[i] > nums[j]:
                    count += 1
            store.append(count)
        return store
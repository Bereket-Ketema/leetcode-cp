class Solution:
    def findKDistantIndices(self, nums, key, k):
        result = []
        right = -1

        for i in range(len(nums)):
            if nums[i] == key:
                start = max(0, i - k)
                end = min(len(nums) - 1, i + k)

                start = max(start, right + 1)

                for j in range(start, end + 1):
                    result.append(j)

                right = end

        return result
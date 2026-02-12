class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            left, right = i , i+1

            while right < len(nums):
                if nums[left] == nums[right] and (left * right) % k == 0:
                    count += 1
                right += 1
        return count
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums.sort()
        
        ans = 0
        left = 0
        
        for right in range(1,len(nums)):
            if abs(nums[left] - nums[right]) == 1:
                temp = freq[nums[left]] + freq[nums[right]]
                ans = max(ans, temp)
            left += 1
        return ans
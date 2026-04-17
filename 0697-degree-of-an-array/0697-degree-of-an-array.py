class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = defaultdict(int)
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
        
        degree = max(count.values())
        ans = len(nums)
        
        for num in count:
            if count[num] == degree:
                length = right[num] - left[num] + 1
                ans = min(ans, length)
        
        return ans
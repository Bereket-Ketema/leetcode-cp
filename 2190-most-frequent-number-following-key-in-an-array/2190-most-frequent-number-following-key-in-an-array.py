from collections import Counter

class Solution:
    def mostFrequent(self, nums, key):
        cnt = Counter()
        
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnt[nums[i + 1]] += 1
        
        return cnt.most_common(1)[0][0]
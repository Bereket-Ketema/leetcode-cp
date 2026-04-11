class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0
        
        n = len(nums)
        size = max(1, (mx - mn) // (n - 1))
        count = (mx - mn) // size + 1
        
        bucket_min = [float('inf')] * count
        bucket_max = [float('-inf')] * count
        used = [False] * count
        
        for num in nums:
            idx = (num - mn) // size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
            used[idx] = True
        
        prev = mn
        res = 0
        
        for i in range(count):
            if not used[i]:
                continue
            res = max(res, bucket_min[i] - prev)
            prev = bucket_max[i]
        
        return res
class Solution:
    def splitArraySameAverage(self, nums):
        n = len(nums)
        s = sum(nums)
        dp = [set() for _ in range(n+1)]
        dp[0].add(0)
        
        for num in nums:
            for i in range(n-1, -1, -1):
                for prev in dp[i]:
                    dp[i+1].add(prev + num)
        
        for i in range(1, n):
            if s * i % n == 0 and (s * i // n) in dp[i]:
                return True
        
        return False
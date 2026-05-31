class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        ans = 0
        
        for i in range(len(timeSeries) - 1):
            ans += min(duration, timeSeries[i + 1] - timeSeries[i])
        
        return ans + duration
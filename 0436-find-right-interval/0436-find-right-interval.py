class Solution:
    def findRightInterval(self, intervals):
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_vals = [s[0] for s in starts]
        
        res = []
        for interval in intervals:
            idx = bisect.bisect_left(start_vals, interval[1])
            if idx < len(intervals):
                res.append(starts[idx][1])
            else:
                res.append(-1)
        
        return res
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        ans = 0
        best = 0
        j = 0
        
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                best = max(best, jobs[j][1])
                j += 1
            
            ans += best
        
        return ans
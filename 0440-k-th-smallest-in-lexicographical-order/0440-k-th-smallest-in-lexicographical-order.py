class Solution:
    def findKthNumber(self, n, k):
        def count(prefix):
            curr, next_ = prefix, prefix + 1
            total = 0
            while curr <= n:
                total += min(n+1, next_) - curr
                curr *= 10
                next_ *= 10
            return total
        
        curr = 1
        k -= 1
        
        while k > 0:
            steps = count(curr)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        
        return curr
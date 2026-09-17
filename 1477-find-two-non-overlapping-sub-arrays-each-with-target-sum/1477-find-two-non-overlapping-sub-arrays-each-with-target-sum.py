class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        left = 0
        curr_sum = 0
        best = float('inf')
        ans = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
                
            if curr_sum == target:
                length = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, length + min_len[left - 1])
                best = min(best, length)
                
            min_len[right] = best
            
        return ans if ans != float('inf') else -1
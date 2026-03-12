
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        diff = [0]*(n+1)

        for l, r in requests:
            diff[l] += 1
            diff[r+1] -= 1

        freq = [0]*n
        cur = 0
        for i in range(n):
            cur += diff[i]
            freq[i] = cur

        nums.sort()
        freq.sort()

        ans = 0
        for a, b in zip(nums, freq):
            ans = (ans + a*b) % MOD

        return ans
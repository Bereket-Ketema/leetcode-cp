class Solution:
    def countTriplets(self, nums):
        from collections import Counter
        cnt = Counter(a & b for a in nums for b in nums)
        return sum(cnt[x] for x in cnt for a in nums if a & x == 0)
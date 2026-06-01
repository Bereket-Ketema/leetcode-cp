from collections import Counter

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        cnt = Counter()

        for a in nums1:
            for b in nums2:
                cnt[a + b] += 1

        ans = 0

        for c in nums3:
            for d in nums4:
                ans += cnt[-(c + d)]

        return ans
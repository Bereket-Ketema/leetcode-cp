from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        cnt = Counter()
        freq = Counter()
        ans = mx = 0

        for i,x in enumerate(nums,1):
            if cnt[x]:
                freq[cnt[x]] -= 1

            cnt[x] += 1
            freq[cnt[x]] += 1
            mx = max(mx, cnt[x])

            if (
                mx == 1 or
                mx*freq[mx] + 1 == i or
                (mx-1)*(freq[mx-1]+1) + 1 == i
            ):
                ans = i

        return ans
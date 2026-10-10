from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        max_diff = max(diffs)
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1

        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue

            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d - 1] += k
                count[d] -= k
                k = 0
                break

        return sum(c * (d ** 2) for d, c in enumerate(count))
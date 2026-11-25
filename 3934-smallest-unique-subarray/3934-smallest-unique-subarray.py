from collections import Counter


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base1, mod1 = 100003, 1_000_000_007
        base2, mod2 = 100019, 1_000_000_009

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base1) % mod1
            pow2[i] = (pow2[i - 1] * base2) % mod2

        def has_unique_length(k: int) -> bool:
            h1 = h2 = 0
            for i in range(k):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            counts = Counter([(h1, h2)])
            high1 = pow1[k - 1]
            high2 = pow2[k - 1]

            for i in range(k, n):
                left = nums[i - k]
                right = nums[i]

                h1 = ((h1 - left * high1) * base1 + right) % mod1
                h2 = ((h2 - left * high2) * base2 + right) % mod2
                counts[(h1, h2)] += 1

            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        res = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        for n in nums:
            prefix += n
            ream = prefix % k

            if ream in prefix_count:
                res += prefix_count[ream]
            prefix_count[ream] += 1
        return res
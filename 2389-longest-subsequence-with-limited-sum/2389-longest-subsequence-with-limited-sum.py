from typing import List
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        answer = []

        for q in queries:
            count = bisect_right(prefix, q) - 1
            answer.append(count)

        return answer
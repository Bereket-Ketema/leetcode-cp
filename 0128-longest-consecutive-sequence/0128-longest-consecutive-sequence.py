class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        count = 0
        for num in store:
            if num - 1 not in store:
                length = 0
                t = num
                while t in store:
                    length += 1
                    t += 1
                count = max(count,length)
        return count
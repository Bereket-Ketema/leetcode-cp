class Solution:
    def maximumCount(self, nums):
        positive = 0
        negative = 0

        for x in nums:
            if x > 0:
                positive += 1
            elif x < 0:
                negative += 1

        return max(positive, negative)
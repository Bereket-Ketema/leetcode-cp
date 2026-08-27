class Solution:
    def minBitFlips(self, start, goal):
        x = start ^ goal
        return x.bit_count()
class Solution:
    def minOperations(self, s):
        change0 = 0  # Pattern: 010101...
        change1 = 0  # Pattern: 101010...

        for i, ch in enumerate(s):
            if ch != str(i % 2):
                change0 += 1
            if ch != str((i + 1) % 2):
                change1 += 1

        return min(change0, change1)
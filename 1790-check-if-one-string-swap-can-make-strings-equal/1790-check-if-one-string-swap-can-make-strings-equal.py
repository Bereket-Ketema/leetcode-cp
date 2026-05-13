class Solution:
    def areAlmostEqual(self, s1, s2):
        diff = []

        for a, b in zip(s1, s2):
            if a != b:
                diff.append((a, b))

        return len(diff) == 0 or (
            len(diff) == 2 and
            diff[0] == diff[1][::-1]
        )
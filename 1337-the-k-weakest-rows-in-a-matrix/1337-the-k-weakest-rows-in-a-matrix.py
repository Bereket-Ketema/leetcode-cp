class Solution:
    def kWeakestRows(self, mat, k):
        strength = [(sum(row), i) for i, row in enumerate(mat)]
        strength.sort()
        return [i for _, i in strength[:k]]
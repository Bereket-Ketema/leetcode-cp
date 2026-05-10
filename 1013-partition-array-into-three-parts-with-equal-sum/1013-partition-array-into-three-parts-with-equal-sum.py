class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)

        if total % 3:
            return False

        target = total // 3
        cur = parts = 0

        for x in arr:
            cur += x
            if cur == target:
                parts += 1
                cur = 0

        return parts >= 3
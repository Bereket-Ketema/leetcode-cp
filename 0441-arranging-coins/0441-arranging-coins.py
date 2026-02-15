class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        count = 0
        k = n
        for i in range(1,n):
            if k - i < 0:
                break
            count += 1
            k = k - i
        return count
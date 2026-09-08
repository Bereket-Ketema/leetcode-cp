class Solution:
    def countCommas(self, n: int) -> int:
        count = 0

        for x in range(1000, n + 1):
            count += (len(str(x)) - 1) // 3

        return count
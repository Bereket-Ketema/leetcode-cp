class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""

        for ch in s:
            num += str(ord(ch) - ord('a') + 1)

        for _ in range(k):
            num = str(sum(int(c) for c in num))

        return int(num)
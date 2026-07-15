class Solution:
    def digitCount(self, num: str) -> bool:
        from collections import Counter

        cnt = Counter(num)

        for i in range(len(num)):
            if cnt[str(i)] != int(num[i]):
                return False

        return True
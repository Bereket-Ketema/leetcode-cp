from collections import Counter

class Solution:
    def findEvenNumbers(self, digits):
        cnt = Counter(digits)
        ans = []

        for num in range(100, 1000, 2):
            need = Counter(map(int, str(num)))

            ok = True
            for d in need:
                if need[d] > cnt[d]:
                    ok = False
                    break

            if ok:
                ans.append(num)

        return ans
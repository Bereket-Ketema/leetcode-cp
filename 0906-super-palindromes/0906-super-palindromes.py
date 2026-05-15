class Solution:
    def superpalindromesInRange(self, left, right):
        l = int(left)
        r = int(right)

        def ispal(x):
            s = str(x)
            return s == s[::-1]

        ans = 0

        for k in range(1, 100000):
            s = str(k)

            p = int(s + s[-2::-1])
            sq = p*p
            if sq > r:
                break
            if sq >= l and ispal(sq):
                ans += 1

            p = int(s + s[::-1])
            sq = p*p
            if sq > r:
                continue
            if sq >= l and ispal(sq):
                ans += 1

        return ans
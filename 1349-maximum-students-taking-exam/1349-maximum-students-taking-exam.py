from functools import lru_cache

class Solution:
    def maxStudents(self, seats):
        m,n = len(seats), len(seats[0])

        valid = []

        for row in seats:
            masks = []

            for mask in range(1<<n):
                ok = True

                for j in range(n):
                    if (mask>>j)&1:
                        if row[j] == '#':
                            ok = False
                        if j>0 and (mask>>(j-1))&1:
                            ok = False

                if ok:
                    masks.append(mask)

            valid.append(masks)

        @lru_cache(None)
        def dp(r, prev):
            if r == m:
                return 0

            ans = 0

            for mask in valid[r]:
                if (mask&(prev<<1)) == 0 and (mask&(prev>>1)) == 0:
                    ans = max(ans,
                        bin(mask).count('1') + dp(r+1, mask)
                    )

            return ans

        return dp(0,0)
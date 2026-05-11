class Solution:
    def tallestBillboard(self, rods):
        dp = {0:0}

        for r in rods:
            cur = dp.copy()

            for diff,height in cur.items():
                dp[diff + r] = max(dp.get(diff+r,0), height)
                ndiff = abs(diff-r)
                dp[ndiff] = max(
                    dp.get(ndiff,0),
                    height + min(diff,r)
                )

        return dp[0]
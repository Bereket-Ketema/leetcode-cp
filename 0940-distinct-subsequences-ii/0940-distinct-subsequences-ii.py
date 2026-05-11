class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        dp = 1
        last = {}

        for c in s:
            new_dp = (dp * 2) % MOD

            if c in last:
                new_dp = (new_dp - last[c]) % MOD

            last[c] = dp
            dp = new_dp

        return (dp - 1) % MOD
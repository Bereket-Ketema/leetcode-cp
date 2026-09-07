class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1

        last = [0] * 26

        for c in s:
            x = ord(c) - ord('a')

            new_dp = (2 * dp - last[x]) % MOD

            last[x] = dp
            dp = new_dp

        return (dp - 1) % MOD
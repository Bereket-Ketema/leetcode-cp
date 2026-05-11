class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        mod = 10**9 + 7
        base = 31

        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            prefix[i + 1] = (prefix[i] * base + (ord(text[i]) - ord('a') + 1)) % mod
            power[i + 1] = (power[i] * base) % mod

        def get_hash(l, r):
            return (prefix[r] - prefix[l] * power[r - l]) % mod

        seen = set()

        for length in range(1, n // 2 + 1):
            for i in range(n - 2 * length + 1):
                h1 = get_hash(i, i + length)
                h2 = get_hash(i + length, i + 2 * length)

                if h1 == h2:
                    seen.add(h1)

        return len(seen)
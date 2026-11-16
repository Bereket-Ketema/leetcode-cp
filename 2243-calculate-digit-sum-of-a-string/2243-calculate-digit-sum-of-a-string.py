class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s = []
            for i in range(0, len(s), k):
                chunk_sum = sum(int(ch) for ch in s[i:i + k])
                next_s.append(str(chunk_sum))
            s = "".join(next_s)
        return s
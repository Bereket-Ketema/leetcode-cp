class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        check = set(freq.values())
        return True if len(check) == 1 else False
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        store = Counter(s)
        check = set(s)
        if letter not in check:
            return 0

        return floor((store[letter] / len(s)) * 100)
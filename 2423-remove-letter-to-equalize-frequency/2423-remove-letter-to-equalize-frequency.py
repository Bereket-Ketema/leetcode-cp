from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)

        for ch in freq:
            freq[ch] -= 1

            values = [v for v in freq.values() if v > 0]

            if values and len(set(values)) == 1:
                return True

            freq[ch] += 1

        return False
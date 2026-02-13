from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        wor1 = Counter(word1)
        wor2 = Counter(word2)
        if sorted(wor1.keys()) == sorted(wor2.keys()) and sorted(wor1.values()) == sorted(wor2.values()):
            return True
        return False
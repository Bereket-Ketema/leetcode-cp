class Solution:
    def checkAlmostEquivalent(self, word1, word2):
        count = [0] * 26

        for c in word1:
            count[ord(c) - ord('a')] += 1

        for c in word2:
            count[ord(c) - ord('a')] -= 1

        for x in count:
            if abs(x) > 3:
                return False

        return True
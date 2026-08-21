class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        broken = set(brokenLetters)
        count = 0

        for word in text.split():
            if all(c not in broken for c in word):
                count += 1

        return count
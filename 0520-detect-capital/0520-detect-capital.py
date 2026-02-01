class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word == word.capitalize() or word == word.lower() or word == word.upper() else False
class Solution:
    def halvesAreAlike(self, s):
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2

        left = sum(c in vowels for c in s[:mid])
        right = sum(c in vowels for c in s[mid:])

        return left == right
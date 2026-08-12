class Solution:
    def countPrefixes(self, words, s):
        ans = 0

        for word in words:
            if s.startswith(word):
                ans += 1

        return ans
from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        store = ""
        for i in range(1,len(s)):
            if int(s[i-1]) != int(s[i]):
                if int(s[i-1]) == freq[s[i-1]] and int(s[i]) == freq[s[i]]:
                    if (s[i-1] not in store) and (s[i] not in store):
                        store += s[i-1]
                        store += s[i]
                        return store
        return store
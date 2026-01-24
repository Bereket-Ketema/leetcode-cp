class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        store = {}
        for i in range(len(t)):
            if t[i] in store:
                store[t[i]] +=1
            else:
                store[t[i]] = 1
        for i in range(len(s)):
            if s[i] in store:
                store[s[i]] -=1
            else:
                store[s[i]] = -1
        for key, value in store.items():
            if value == 1:
                return key
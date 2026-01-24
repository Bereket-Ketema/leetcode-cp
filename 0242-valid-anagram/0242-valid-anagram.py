class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            store = {}
            for i in range(len(s)):
                if s[i] in store:
                    store[s[i]] +=1
                else:
                    store[s[i]] = 1 
                if t[i] in store:
                    store[t[i]] -=1
                else:
                    store[t[i]] = -1
        return True  if all(value == 0 for value in store.values())  else False
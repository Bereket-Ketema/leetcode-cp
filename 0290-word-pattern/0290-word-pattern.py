class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        store = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in store:
                if words[i] not in store.values():
                    store[pattern[i]] = words[i]
                else:
                    return False
            elif pattern[i] in store and words[i] != store[pattern[i]]:
                return False
        return True
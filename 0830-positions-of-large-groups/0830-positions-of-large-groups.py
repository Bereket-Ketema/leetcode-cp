class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        store = []
        e = 1
        count, first = 1, 0
        for i in range(len(s)-1):
            if s[i] == s[e]:
                if count == 1:
                    first = i
                count += 1
            if s[i] != s[e]:
                if count >= 3:
                    store.append([first,i])
                count = 1
                first = 0
            if e == len(s)-1 and count >=3:
                store.append([first,i+1])
            e += 1
        return store
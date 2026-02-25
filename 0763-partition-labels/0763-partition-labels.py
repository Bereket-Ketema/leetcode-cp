class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        store = []

        for i, ch in enumerate(s):
            last_index[ch] = i
        
        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            if last_index[s[i]] > end:
                end = last_index[s[i]]

            if i == end:
                store.append(size)
                size = 0

        return store
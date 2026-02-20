class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        order = list(order)
        store = ""
        for i in order:
            if i in s:
                store += i * freq[i]
                del freq[i]
        for i in freq:
            store += i * freq[i]
        return store
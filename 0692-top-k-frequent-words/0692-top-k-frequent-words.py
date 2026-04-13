from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        return sorted(count.keys(), key=lambda x: (-count[x], x))[:k]
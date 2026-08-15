class Solution:
    def mergeSimilarItems(self, items1, items2):
        freq = {}

        for value, weight in items1:
            freq[value] = freq.get(value, 0) + weight

        for value, weight in items2:
            freq[value] = freq.get(value, 0) + weight

        return [[value, freq[value]] for value in sorted(freq)]
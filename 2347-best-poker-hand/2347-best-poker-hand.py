from collections import Counter

class Solution:
    def bestHand(self, ranks, suits):
        if len(set(suits)) == 1:
            return "Flush"

        count = Counter(ranks)
        max_count = max(count.values())

        if max_count >= 3:
            return "Three of a Kind"

        if max_count == 2:
            return "Pair"

        return "High Card"
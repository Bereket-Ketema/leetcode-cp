from collections import defaultdict
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(2 * f, max_factor + 1, f):
                    freq[f] += freq[multiple]

        cost_slots = defaultdict(int)
        for factor, price in items:
            free_slots = freq[factor] - 1
            if free_slots > 0 and price <= 2 * cheapest:
                cost_slots[price] += free_slots

        total_items = 0
        for price in sorted(cost_slots):
            slots = cost_slots[price]
            buy = min(slots, budget // price)
            total_items += 2 * buy
            budget -= buy * price

        total_items += budget // cheapest
        return total_items
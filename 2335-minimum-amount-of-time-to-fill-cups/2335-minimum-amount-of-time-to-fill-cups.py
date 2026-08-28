class Solution:
    def fillCups(self, amount):
        total = sum(amount)
        maximum = max(amount)

        return max(maximum, (total + 1) // 2)
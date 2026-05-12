class Solution:
    def timeRequiredToBuy(self, tickets, k):
        ans = 0

        for i, x in enumerate(tickets):
            if i <= k:
                ans += min(x, tickets[k])
            else:
                ans += min(x, tickets[k]-1)

        return ans
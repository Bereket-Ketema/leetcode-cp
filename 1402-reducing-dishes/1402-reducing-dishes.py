class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)

        ans = total = 0

        for x in satisfaction:
            total += x

            if total <= 0:
                break

            ans += total

        return ans
class Solution:
    def maximumPopulation(self, logs):
        years = [0] * 101  # 1950 - 2050

        for birth, death in logs:
            years[birth - 1950] += 1
            years[death - 1950] -= 1

        ans = 1950
        cur = 0
        mx = 0

        for i in range(101):
            cur += years[i]
            if cur > mx:
                mx = cur
                ans = 1950 + i

        return ans
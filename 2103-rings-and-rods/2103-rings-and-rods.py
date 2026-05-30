class Solution:
    def countPoints(self, rings):
        rods = [set() for _ in range(10)]

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rods[rod].add(color)

        return sum(len(s) == 3 for s in rods)
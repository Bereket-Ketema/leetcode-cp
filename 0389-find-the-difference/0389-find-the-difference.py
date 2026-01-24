class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        g = list(t)
        print(g)
        for i in s:
            if i in g:
                g.remove(i)
        return g[0]
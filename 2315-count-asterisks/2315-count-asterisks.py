class Solution:
    def countAsterisks(self, s):
        count = 0
        inside = False

        for c in s:
            if c == '|':
                inside = not inside
            elif c == '*' and not inside:
                count += 1

        return count
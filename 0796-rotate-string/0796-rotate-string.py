class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        sl = list(s)
        goalL = list(goal)
        while True:
            sl.append(sl[0])
            sl.pop(0)
            if sl == goalL:
                return True
            if "".join(sl) == s:
                break
        return False
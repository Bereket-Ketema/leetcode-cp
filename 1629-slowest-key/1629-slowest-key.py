class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        best = releaseTimes[0]
        ans = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i-1]

            if dur > best or (dur == best and keysPressed[i] > ans):
                best = dur
                ans = keysPressed[i]

        return ans
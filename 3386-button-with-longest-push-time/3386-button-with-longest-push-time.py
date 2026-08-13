class Solution:
    def buttonWithLongestTime(self, events):
        ans = events[0][0]
        longest = events[0][1]

        for i in range(1, len(events)):
            duration = events[i][1] - events[i - 1][1]

            if duration > longest:
                longest = duration
                ans = events[i][0]
            elif duration == longest:
                ans = min(ans, events[i][0])

        return ans
class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        left = [n] * 26
        right = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = i

        intervals = []

        for i in range(26):
            if right[i] == -1:
                continue

            l = left[i]
            r = right[i]
            j = l

            valid = True
            while j <= r:
                c = ord(s[j]) - ord('a')
                if left[c] < l:
                    valid = False
                    break
                r = max(r, right[c])
                j += 1

            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        res = []
        end = -1

        for l, r in intervals:
            if l > end:
                res.append(s[l:r + 1])
                end = r

        return res
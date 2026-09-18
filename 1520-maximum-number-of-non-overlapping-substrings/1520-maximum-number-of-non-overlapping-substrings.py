class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for ch in set(s):
            l = first[ch]
            r = last[ch]
            valid = True
            i = l
            while i <= r:
                if first[s[i]] < l:
                    valid = False
                    break
                r = max(r, last[s[i]])
                i += 1
            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                ans.append(s[l : r + 1])
                last_end = r

        return ans
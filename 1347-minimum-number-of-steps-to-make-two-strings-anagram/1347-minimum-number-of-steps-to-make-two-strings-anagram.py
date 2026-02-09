from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = Counter(s)
        count = 0
        for let in t:
          if freq[let] != 0:
            freq[let] -= 1
          else:
             count += 1
        return count
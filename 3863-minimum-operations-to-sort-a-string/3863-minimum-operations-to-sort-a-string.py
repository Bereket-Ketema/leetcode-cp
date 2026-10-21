class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_s = "".join(sorted(s))
        
        if s == sorted_s:
            return 0
        
        if n <= 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        if s[0] == max_char and s[-1] == min_char:
            count_min = s.count(min_char)
            count_max = s.count(max_char)
            if count_min == 1 and count_max == 1:
                return 3
            return 2
        
        return 2
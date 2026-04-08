class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_types = int(any(c.islower() for c in s)) + \
                        int(any(c.isupper() for c in s)) + \
                        int(any(c.isdigit() for c in s))
        missing_types = 3 - missing_types
        
        change = 0
        one = two = 0
        i = 2
        
        n = len(s)
        while i < n:
            if s[i] == s[i-1] == s[i-2]:
                length = 2
                while i < n and s[i] == s[i-1]:
                    length += 1
                    i += 1
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1
        
        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, change)
        else:
            delete = n - 20
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing_types, change)
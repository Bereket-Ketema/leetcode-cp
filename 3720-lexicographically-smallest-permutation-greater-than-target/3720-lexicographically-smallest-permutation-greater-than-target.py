from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_count = Counter(s)
        prefix_count = Counter(target)
        
        # Check from the longest possible common prefix down to length 0
        for i in range(n - 1, -1, -1):
            # Update prefix_count so it represents target[:i]
            prefix_count[target[i]] -= 1
            if prefix_count[target[i]] == 0:
                del prefix_count[target[i]]
            
            # Check if target[:i] can be formed using the characters in s
            if all(prefix_count[ch] <= s_count[ch] for ch in prefix_count):
                # Calculate available remaining characters
                rem_count = s_count.copy()
                for ch, count in prefix_count.items():
                    rem_count[ch] -= count
                
                # Pick the smallest available character strictly greater than target[i]
                for code in range(ord(target[i]) + 1, ord('z') + 1):
                    c = chr(code)
                    if rem_count[c] > 0:
                        rem_count[c] -= 1
                        
                        # Append the rest of the available characters in sorted order
                        suffix = "".join(
                            chr(k) * rem_count[chr(k)]
                            for k in range(ord('a'), ord('z') + 1)
                        )
                        
                        return target[:i] + c + suffix
                        
        return ""
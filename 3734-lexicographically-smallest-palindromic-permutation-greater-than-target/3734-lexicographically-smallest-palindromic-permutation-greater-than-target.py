from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        odd_chars = [c for c, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > (1 if n % 2 != 0 else 0):
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: counts[c] // 2 for c in counts}
        m = n // 2

        def can_form_prefix(prefix_len: int) -> bool:
            needed = Counter(target[:prefix_len])
            return all(half_counts.get(c, 0) >= count for c, count in needed.items())

        if can_form_prefix(m):
            prefix = target[:m]
            if n % 2 != 0:
                full_pal = prefix + mid_char + prefix[::-1]
            else:
                full_pal = prefix + prefix[::-1]
            
            if full_pal > target:
                return full_pal

        for i in range(m - 1, -1, -1):
            if not can_form_prefix(i):
                continue
            
            used = Counter(target[:i])
            avail = {c: half_counts[c] - used.get(c, 0) for c in half_counts}
            
            for o in range(ord(target[i]) - ord('a') + 1, 26):
                c = chr(ord('a') + o)
                if avail.get(c, 0) > 0:
                    avail[c] -= 1
                    
                    rest_first_half = []
                    for code in range(26):
                        ch = chr(ord('a') + code)
                        if avail.get(ch, 0) > 0:
                            rest_first_half.append(ch * avail[ch])
                    
                    first_half = target[:i] + c + "".join(rest_first_half)
                    
                    if n % 2 != 0:
                        return first_half + mid_char + first_half[::-1]
                    else:
                        return first_half + first_half[::-1]

        return ""
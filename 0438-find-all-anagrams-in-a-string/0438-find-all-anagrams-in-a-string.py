class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        window = Counter()
        result = []
        k = 0

        if len(p) > len(s):
            k = len(s)
        else:
            k = len(p)

        for i in range(k):
            window[s[i]] += 1

        if window == p_count:
            result.append(0)
        
        left = 0
        for right in range(k, len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]

            if window == p_count:
                result.append(left+1)
            
            left += 1
        
        return result


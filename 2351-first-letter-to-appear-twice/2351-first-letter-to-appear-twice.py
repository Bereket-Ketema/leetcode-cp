class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for i in range(len(s)):
            if s[i] in seen:
                return s[i]

            seen.add(s[i])
            
        return ''
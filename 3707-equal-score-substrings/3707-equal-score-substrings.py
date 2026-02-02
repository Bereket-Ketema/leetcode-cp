class Solution:
    def scoreBalance(self, s: str) -> bool:
        left = ord(s[0]) - 96
        right = 0
        for i in range(1,len(s)):
            right += ord(s[i]) - 96
        for j in range(1,len(s)):
            if left == right:
                return True
            right = right -( ord(s[j]) - 96 )
            left += ord(s[j]) - 96
        return False
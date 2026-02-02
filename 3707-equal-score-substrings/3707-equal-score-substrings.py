class Solution:
    def scoreBalance(self, s: str) -> bool:
        left = 0
        right = 0
        for i in range(len(s)):
            left += ord(s[i]) - 96
            for j in range(i+1,len(s)):
                right += ord(s[j]) - 96
            if left == right:
                return True
            right = 0
        return False
class Solution:
    def longestDecomposition(self, text):
        n = len(text)
        
        for length in range(1, n // 2 + 1):
            if text[:length] == text[n-length:]:
                return 2 + self.longestDecomposition(text[length:n-length])
        
        return 1 if text else 0
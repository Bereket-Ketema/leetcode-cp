class Solution:
    def getHint(self, secret, guess):
        bulls = sum(s == g for s, g in zip(secret, guess))
        
        from collections import Counter
        s_count = Counter(secret)
        g_count = Counter(guess)
        
        cows = sum(min(s_count[k], g_count[k]) for k in s_count) - bulls
        
        return f"{bulls}A{cows}B"
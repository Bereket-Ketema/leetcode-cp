class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        
        def can(word):
            if not word:
                return False
            dp = [False]*(len(word)+1)
            dp[0] = True
            
            for i in range(1, len(word)+1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        if j == 0 and i == len(word):
                            continue
                        dp[i] = True
                        break
            return dp[-1]
        
        res = []
        for word in words:
            word_set.remove(word)
            if can(word):
                res.append(word)
            word_set.add(word)
        
        return res
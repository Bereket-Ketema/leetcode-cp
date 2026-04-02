class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)

        @lru_cache(None)
        def dfs(start):
            if start == len(s):
                return [""]

            res = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            return res

        return dfs(0)
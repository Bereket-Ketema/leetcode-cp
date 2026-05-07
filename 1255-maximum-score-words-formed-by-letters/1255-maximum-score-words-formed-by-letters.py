from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        cnt = Counter(letters)
        n = len(words)

        def dfs(i, cur):
            if i == n:
                return cur

            res = dfs(i+1, cur)

            need = Counter(words[i])
            ok = True
            add = 0

            for c,v in need.items():
                if cnt[c] < v:
                    ok = False
                    break

                add += score[ord(c)-97]*v

            if ok:
                for c,v in need.items():
                    cnt[c] -= v

                res = max(res, dfs(i+1, cur+add))

                for c,v in need.items():
                    cnt[c] += v

            return res

        return dfs(0,0)
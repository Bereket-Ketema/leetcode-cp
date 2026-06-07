class Solution:
    def sortSentence(self, s: str) -> str:
        result = [(word[:-1], int(word[-1])) for word in s.split()]
        result = sorted(result, key=lambda x: x[1])
        
        ans = ''
        for i in range(len(result)):
            ans += result[i][0] + ' '
        
        return ans[:-1]

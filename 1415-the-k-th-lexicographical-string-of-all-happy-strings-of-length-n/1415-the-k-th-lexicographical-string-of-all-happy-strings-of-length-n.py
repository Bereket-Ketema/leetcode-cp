class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def backtrack(path):
            if len(path) == n:
                res.append(path)
                return
            
            for ch in ['a', 'b', 'c']:
                if path and path[-1] == ch:
                    continue
                
                backtrack(path + ch)
        
        backtrack("")
        
        return res[k-1] if k <= len(res) else ""
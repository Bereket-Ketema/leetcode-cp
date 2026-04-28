class Solution:
    def diffWaysToCompute(self, expression):
        memo = {}
        
        def dfs(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res
        
        return dfs(expression)
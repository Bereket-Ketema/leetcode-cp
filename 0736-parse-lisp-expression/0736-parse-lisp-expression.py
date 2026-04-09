class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(expr, scope):
            if expr[0] != '(':
                return int(expr) if expr[0].isdigit() or expr[0] == '-' else scope[expr]
            
            parts = []
            bal = 0
            start = 1
            for i, ch in enumerate(expr):
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                elif ch == ' ' and bal == 1:
                    parts.append(expr[start:i])
                    start = i+1
            parts.append(expr[start:-1])
            
            if parts[0] == "add":
                return parse(parts[1], scope.copy()) + parse(parts[2], scope.copy())
            if parts[0] == "mult":
                return parse(parts[1], scope.copy()) * parse(parts[2], scope.copy())
            
            for i in range(1, len(parts)-1, 2):
                scope[parts[i]] = parse(parts[i+1], scope.copy())
            return parse(parts[-1], scope.copy())
        
        return parse(expression, {})
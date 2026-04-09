from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        
        while i < len(formula):
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                mult = int(formula[i_start:i] or 1)
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k] * mult
            else:
                i_start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][name] += count
        
        return "".join(k + (str(v) if v > 1 else "") for k, v in sorted(stack[-1].items()))
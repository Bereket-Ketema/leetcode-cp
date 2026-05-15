from collections import Counter

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        vals = dict(zip(evalvars, evalints))

        def merge(a, b, sign=1):
            res = Counter(a)
            for k,v in b.items():
                res[k] += sign*v
            return res

        def multiply(a, b):
            res = Counter()
            for x,v1 in a.items():
                for y,v2 in b.items():
                    key = tuple(sorted(x+y))
                    res[key] += v1*v2
            return res

        def parse(expr):
            stack = []
            op = '+'
            i = 0

            while i < len(expr):
                if expr[i] == ' ':
                    i += 1
                    continue

                if expr[i].isdigit():
                    j = i
                    while j < len(expr) and expr[j].isdigit():
                        j += 1
                    val = Counter({(): int(expr[i:j])})
                    i = j

                elif expr[i].isalpha():
                    j = i
                    while j < len(expr) and expr[j].isalpha():
                        j += 1
                    var = expr[i:j]
                    if var in vals:
                        val = Counter({(): vals[var]})
                    else:
                        val = Counter({(var,):1})
                    i = j

                elif expr[i] == '(':
                    bal = 1
                    j = i+1
                    while bal:
                        if expr[j] == '(':
                            bal += 1
                        elif expr[j] == ')':
                            bal -= 1
                        j += 1
                    val = parse(expr[i+1:j-1])
                    i = j

                else:
                    op = expr[i]
                    i += 1
                    continue

                if not stack:
                    stack.append(val)
                elif op == '*':
                    stack[-1] = multiply(stack[-1], val)
                elif op == '+':
                    stack.append(val)
                else:
                    stack.append(Counter({k:-v for k,v in val.items()}))

            res = Counter()
            for x in stack:
                res = merge(res, x)

            return res

        poly = parse(expression)

        ans = []
        items = sorted(poly.items(), key=lambda x:(-len(x[0]), x[0]))

        for vars_, coef in items:
            if coef == 0:
                continue
            term = str(coef)
            for v in vars_:
                term += "*" + v
            ans.append(term)

        return ans
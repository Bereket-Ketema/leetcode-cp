class Solution:
    def braceExpansionII(self, expression):
        def helper(expr):
            stack = []
            cur = {""}
            i = 0

            while i < len(expr):
                if expr[i].isalpha():
                    cur = {a+expr[i] for a in cur}
                
                elif expr[i] == '{':
                    bal = 1
                    j = i+1

                    while bal:
                        if expr[j] == '{':
                            bal += 1
                        elif expr[j] == '}':
                            bal -= 1
                        j += 1

                    sub = helper(expr[i+1:j-1])
                    cur = {a+b for a in cur for b in sub}
                    i = j-1

                elif expr[i] == ',':
                    stack.extend(cur)
                    cur = {""}

                i += 1

            stack.extend(cur)
            return set(stack)

        return sorted(helper(expression))
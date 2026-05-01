class Solution:
    def parseBoolExpr(self, expr):
        stack=[]
        for c in expr:
            if c in ',': continue
            if c != ')':
                stack.append(c)
            else:
                seen=set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()
                op = stack.pop()
                if op=='!':
                    stack.append('t' if 'f' in seen else 'f')
                elif op=='&':
                    stack.append('f' if 'f' in seen else 't')
                else:
                    stack.append('t' if 't' in seen else 'f')
        return stack[0]=='t'
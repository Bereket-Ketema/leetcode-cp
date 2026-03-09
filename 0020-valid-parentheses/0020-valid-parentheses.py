class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        is_valid = True

        matching = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if stack and stack[-1] == matching[c]:
                    stack.pop()
                else:
                    is_valid = False
                    break
        return(is_valid and len(stack) == 0)
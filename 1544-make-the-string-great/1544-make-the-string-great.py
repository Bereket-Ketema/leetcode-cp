class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
            if  stack:
                if stack[-1].lower() == s[i].lower() and stack[-1] != s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return ''.join(stack)

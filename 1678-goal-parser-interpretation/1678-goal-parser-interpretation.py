class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        ans = ''

        for i in range(len(command)):
            if stack:
                if command[i] == ')':
                    ans += 'o'
                stack.pop()
            
            if command[i] == '(':
                stack.append('(')
            
            if command[i] == 'a' or command[i] == 'l' or command[i] == 'G':
                ans += command[i]
            
        return ans
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        store = path.split('/')
        for i in store:
            if i != "." and i != "":
                if i == ".." and stack:
                    stack.pop()
                elif i != "..":
                    stack.append(i)
        
        return "/" + "/".join(stack) if stack else "/"

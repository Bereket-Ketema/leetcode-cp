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
        print(stack)
        ans = ""
        for i in stack:
            if i != "":
                ans += "/"
                ans += i
        return ans if ans else "/"

class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)

        while i < n:
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 3

            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i+2:j]
                if not (1 <= len(tag) <= 9 and tag.isupper()):
                    return False

                if not stack or stack[-1] != tag:
                    return False

                stack.pop()
                i = j + 1

            elif code.startswith("<", i):
                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i+1:j]

                if not tag or len(tag) > 9:
                    return False
                for ch in tag:
                    if not ('A' <= ch <= 'Z'):
                        return False

                stack.append(tag)
                i = j + 1

            else:
                i += 1

        return len(stack) == 0
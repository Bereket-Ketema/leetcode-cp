class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                store = ""
                number = ""

                while stack and stack[-1] != "[":
                    store = stack.pop() + store

                stack.pop()

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(store * int(number))

        return "".join(stack)
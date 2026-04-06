class Solution:
    def removeInvalidParentheses(self, s: str):
        if not s:
            return [""]

        res = []
        visited = set()
        queue = deque([s])
        found = False

        while queue:
            level_size = len(queue)
            current_level = set()

            for _ in range(level_size):
                expr = queue.popleft()

                if self.isValid(expr):
                    res.append(expr)
                    found = True

                if found:
                    continue

                for i in range(len(expr)):
                    if expr[i] not in ('(', ')'):
                        continue
                    next_expr = expr[:i] + expr[i+1:]
                    if next_expr not in visited:
                        queue.append(next_expr)
                        visited.add(next_expr)

            if found:
                break 

        return res

    def isValid(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                stackT, stackI = stack.pop()
                res[stackI] = (i- stackI)   

            stack.append([num, i])
        return res
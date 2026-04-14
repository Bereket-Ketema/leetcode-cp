class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            c = set(i)
            if target in c:
                return True
        return False
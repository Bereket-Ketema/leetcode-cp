class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while top < bottom and left < right:

            #for the top row
            for i in range(left, right):
                num.append(matrix[top][i])
            top += 1

            #for the right column
            for i in range(top, bottom):
                num.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            #for the bottom row
            for i in range(right-1, left-1, -1):
                num.append(matrix[bottom-1][i])
            bottom -= 1

            #for the left column
            for i in range(bottom-1, top-1, -1):
                num.append(matrix[i][left])
            left += 1
        return num
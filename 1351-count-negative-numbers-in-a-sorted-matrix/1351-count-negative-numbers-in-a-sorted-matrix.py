class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        l,count=0,0
        for i in range(len(grid)):

            while l<len(grid[i]):
                if grid[i][l] < 0:
                    count+=1
                l+=1
            l=0
        return count
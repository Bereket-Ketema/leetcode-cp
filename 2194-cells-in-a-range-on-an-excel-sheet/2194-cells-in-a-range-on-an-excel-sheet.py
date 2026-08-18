class Solution:
    def cellsInRange(self, s):
        result = []

        start_col = s[0]
        start_row = int(s[1])
        end_col = s[3]
        end_row = int(s[4])

        for col in range(ord(start_col), ord(end_col) + 1):
            for row in range(start_row, end_row + 1):
                result.append(chr(col) + str(row))

        return result
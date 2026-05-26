class Solution:
    def tictactoe(self, moves):
        board = [[""] * 3 for _ in range(3)]
        
        for i, (r, c) in enumerate(moves):
            board[r][c] = "A" if i % 2 == 0 else "B"
        
        lines = []

        for i in range(3):
            lines.append(board[i])
            lines.append([board[0][i], board[1][i], board[2][i]])
        
        lines.append([board[0][0], board[1][1], board[2][2]])
        lines.append([board[0][2], board[1][1], board[2][0]])

        for line in lines:
            if line == ["A", "A", "A"]:
                return "A"
            if line == ["B", "B", "B"]:
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"
class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9+7
        n = len(board)

        score = [[-1]*n for _ in range(n)]
        ways = [[0]*n for _ in range(n)]

        score[n-1][n-1] = 0
        ways[n-1][n-1] = 1

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j] == 'X':
                    continue

                for ni,nj in [(i+1,j),(i,j+1),(i+1,j+1)]:
                    if ni<n and nj<n and score[ni][nj] != -1:
                        val = score[ni][nj]

                        if board[i][j].isdigit():
                            val += int(board[i][j])

                        if val > score[i][j]:
                            score[i][j] = val
                            ways[i][j] = ways[ni][nj]

                        elif val == score[i][j]:
                            ways[i][j] = (ways[i][j] + ways[ni][nj]) % MOD

        if score[0][0] == -1:
            return [0,0]

        return [score[0][0], ways[0][0]]
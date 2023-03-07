def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            ans = True
            if (board[i][j] == 1):
                ans = False
            if (i > 0):
                if (j > 0 and board[i-1][j-1] == 1):
                    ans = False
                if (j < len(board) - 1 and board[i-1][j+1] == 1):
                    ans = False
                if (board[i-1][j] == 1):
                    ans = False
            if (j < len(board) - 1 and board[i][j+1] == 1):
                ans = False
            if (j > 0 and board[i][j-1] == 1):
                ans = False
            if (i < len(board) - 1):
                if (board[i+1][j] == 1):
                    ans = False
                if (j < len(board) - 1 and board[i+1][j+1] == 1):
                    ans = False
                if (j > 0 and board[i+1][j-1] == 1):
                    ans = False
            if (ans == False):
                answer += 1
    return (len(board) * len(board)) - answer
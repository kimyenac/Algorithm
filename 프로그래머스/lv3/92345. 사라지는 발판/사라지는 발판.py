import sys
sys.setrecursionlimit(10 ** 6)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# a 차례
def aturn(ax, ay, bx, by, cnt, board):
    if board[ax][ay] == 0:
        return (1, cnt)
    winner = []
    loser = []
    discrim = False
    for k in range(4):
        nx, ny = ax+dx[k], ay+dy[k]
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1:
            discrim = True
            temp = [row[:] for row in board]
            temp[ax][ay] = 0
            iswin, turn = bturn(bx,by,nx,ny,cnt+1,temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if discrim:
        if winner:
            return (0, min(winner))
        else:
            return (1, max(loser))
    else:
        return (1, cnt)

# b 차례
def bturn(bx, by, ax, ay, cnt, board):
    if board[bx][by] == 0:
        return (1, cnt)
    winner = []
    loser = []
    discrim = False
    for k in range(4):
        nx, ny = bx + dx[k], by + dy[k]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            discrim = True
            temp = [row[:] for row in board]
            temp[bx][by] = 0
            iswin, turn = aturn(ax, ay, nx, ny, cnt + 1, temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if discrim:
        if winner:
            return (0, min(winner))
        else:
            return (1, max(loser))
    else:
        return (1, cnt)

def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    ax, ay, bx, by = aloc[0], aloc[1], bloc[0], bloc[1]

    answer = aturn(ax, ay, bx, by, 0, board)[1]

    return answer
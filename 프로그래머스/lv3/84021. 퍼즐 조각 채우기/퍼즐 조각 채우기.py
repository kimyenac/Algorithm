from copy import deepcopy
def dfs(graph, x, y, position, n, num):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ret = [position]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            ret = ret + dfs(graph, nx, ny, [position[0] + dx[k], position[1] + dy[k]], n, num)

    return ret

# table을 90도, 180도 270도 360도 회전
def rotate(table):
    n = len(table)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = table[i][j]
    return ret

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    
    game_boards = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                game_board[i][j] = 2
                ans = dfs(game_board, i, j, [0, 0], n, 0)[1:]
                game_boards.append(ans)

    for _ in range(4):
        table = rotate(table)
        table_copy = deepcopy(table)
        for i in range(n):
            for j in range(n):
                if table_copy[i][j] == 1:
                    table_copy[i][j] = 2
                    result = dfs(table_copy, i, j, [0, 0], n, 1)[1:]
                    if result in game_boards:
                        game_boards.pop(game_boards.index(result))
                        answer += (len(result)) + 1
                        table = deepcopy(table_copy)
                    else:
                        table_copy = deepcopy(table)

    return answer
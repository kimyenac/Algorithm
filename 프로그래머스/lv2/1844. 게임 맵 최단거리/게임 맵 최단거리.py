from collections import deque
def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    chkb = [[False] * m for i in range(n)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        chkb[x][y] = True
        while q:
            ex, ey = q.popleft()
            for k in range(4):
                nx = ex + dx[k]
                ny = ey + dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if chkb[nx][ny] == False and maps[nx][ny] == 1:
                        chkb[nx][ny] = True
                        maps[nx][ny] = maps[ex][ey] + 1
                        q.append((nx, ny))
    
    bfs(0, 0)
    answer = maps[n-1][m-1]
    if answer > 1:
        return answer
    else:
        return -1
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, graph, chkb):
    q = deque()
    q.append((x, y))
    chkb[x][y] = True
    while q:
        ex, ey = q.popleft()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<m and not chkb[nx][ny]:
                if graph[nx][ny] == "O" and graph[ex][ey] != "O":
                    q.append((nx, ny))
                    chkb[nx][ny] = True
                elif graph[nx][ny] == "P":
                    return False
    return True

def solution(places):
    global n, m
    answer = []
    n = len(places)
    m = len(places[0])

    for place in places:
        chkb = [[False] * m for _ in range(n)]
        discrim = True
        for i in range(n):
            for j in range(m):
                if not chkb[i][j] and place[i][j] == "P":
                    chkb[i][j] = True
                    if not bfs(i, j, place, chkb):
                        discrim = False
                        break
        if discrim:
            answer.append(1)
        else:
            answer.append(0)

    return answer
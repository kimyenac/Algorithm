from collections import deque
def solution(board):

    answer = float("INF")
    n = len(board)
    chkb = [[[float("INF")] * n for _ in range(n)] for _ in range(4)]

    dx = [1, 0, -1, 0]  # 하 우 상 좌
    dy = [0, 1, 0, -1]
    dd = [0, 1, 2, 3]

    def bfs():
        q = deque()
        q.append((0, 0, 0, 0))
        q.append((0, 0, 0, 1))
        while q:
            ex, ey, c, d = q.popleft()
            for k in range(4):
                nx = ex + dx[k]
                ny = ey + dy[k]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    cost = c + 100
                    if d != dd[k]:
                        cost += 500
                    if chkb[dd[k]][nx][ny] > cost:
                        chkb[dd[k]][nx][ny] = cost
                        if nx == n - 1 and ny == n - 1:
                            continue
                        q.append((nx, ny, cost, k))

    bfs()

    for k in range(4):
        answer = min(answer, chkb[k][n-1][n-1])

    return answer
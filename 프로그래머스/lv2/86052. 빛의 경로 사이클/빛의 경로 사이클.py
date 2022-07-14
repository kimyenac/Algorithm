def solution(grid):
    answer = []

    d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    right = {0: 3, 1: 2, 2: 0, 3: 1}
    left = {0: 2, 1: 3, 2: 1, 3: 0}
    n, m = len(grid), len(grid[0])
    chkb = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                if chkb[i][j][k]:
                    continue
                cnt = 0
                nx, ny, nk = i, j, k
                while True:
                    chkb[nx][ny][nk] = True
                    cnt += 1
                    now = grid[nx][ny]
                    if now == "L":
                        nk = left[nk]
                    elif now == "R":
                        nk = right[nk]
                    nx, ny = (nx+d[nk][0]) % n, (ny+d[nk][1])%m
                    if nx == i and ny == j and nk == k:
                        break
                answer.append(cnt)
    answer.sort()
    return answer
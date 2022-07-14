import heapq
def solution(land, height):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    n = len(land)
    heap = [[0, 0, 0]]
    answer = 0
    chkb = [[False] * n for _ in range(n)]
    
    while heap:
        c, ex, ey = heapq.heappop(heap)
        if chkb[ex][ey]:
            continue
        chkb[ex][ey] = True
        answer += c
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<n and not chkb[nx][ny]:
                if abs(land[ex][ey] - land[nx][ny]) <= height:
                    heapq.heappush(heap, [0, nx, ny])
                else:
                    heapq.heappush(heap, [abs(land[ex][ey] - land[nx][ny]), nx, ny])
    
    return answer
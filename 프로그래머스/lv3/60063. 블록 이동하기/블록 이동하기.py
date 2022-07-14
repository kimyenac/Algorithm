from collections import deque
def bfs(cur1, cur2, cnt):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    y, x = 0, 1
    ans = []
    for dy, dx in dxy:
        nxt1 = (cur1[y] + dy, cur1[x] + dx)
        nxt2 = (cur2[y] + dy, cur2[x] + dx)
        if graph[nxt1[y]][nxt1[x]] == 0 and graph[nxt2[y]][nxt2[x]] == 0:
            ans.append((nxt1, nxt2))
            
    if cur1[y] == cur2[y]:
        up, down = -1, 1
        for d in [up, down]:
            if graph[cur1[y]+d][cur1[x]] == 0 and graph[cur2[y]+d][cur2[x]] == 0:
                ans.append((cur1, (cur1[y]+d, cur1[x])))
                ans.append((cur2, (cur2[y]+d, cur2[x])))
    else:
        left, right = -1, 1
        for d in [left, right]:
            if graph[cur1[y]][cur1[x]+d] == 0 and graph[cur2[y]][cur2[x]+d] == 0:
                ans.append((cur1, (cur1[y], cur1[x]+d)))
                ans.append((cur2, (cur2[y], cur2[x]+d)))
    return ans
    

def solution(board):
    global graph
    n = len(board)
    graph = [[1] * (n+2) for _ in range(n+2)]
    
    for i in range(n):
        for j in range(n):
            graph[i+1][j+1] = board[i][j]
    
    chkb = set([((1, 1), (1, 2))])

    q = deque()
    q.append(((1, 1), (1, 2), 0))
    while q:
        cur1, cur2, cnt = q.popleft()
        if cur1 == (n, n) or cur2 == (n, n):
            return cnt
        for nxt in bfs(cur1, cur2, graph):
            if nxt not in chkb:
                q.append((*nxt, cnt+1))
                chkb.add(nxt)
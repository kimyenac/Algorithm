from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    chkb = [False] * (n+1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        q = deque()
        q.append(start)
        chkb[start] = True
        while q:
            x = q.popleft()
            for next in graph[x]:
                if chkb[next] == False:
                    chkb[next] = chkb[x] + 1
                    q.append(next)
    
    bfs(1)
    
    maxy = max(chkb)
    answer = chkb.count(maxy)
    
    return answer
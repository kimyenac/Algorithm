from collections import deque
def bfs(start, chkb, graph):
    q = deque([start])
    ans = 1
    chkb[start] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if chkb[i] == False:
                chkb[i] = True
                ans += 1
                q.append(i)
    return ans

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for start, notVisted in wires:
        chkb = [False] * (n + 1)
        chkb[notVisted] = True
        ans = bfs(start, chkb, graph)
        if abs(ans - (n-ans)) < answer:
            answer = abs(ans - (n-ans))

    return answer
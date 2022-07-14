from collections import deque
def solution(n, computers):

    answer = 0
    network = [[] for _ in range(n)]
    chkb = [False] * n

    def bfs(network, start, chkb):
        q = deque()
        q.append(start)
        chkb[start] = True
        while q:
            x = q.popleft()
            for k in network[x]:
                if not chkb[k]:
                    q.append(k)
                    chkb[k] = True

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                network[i].append(j)

    for i in range(len(computers)):
        if not chkb[i]:
            bfs(network, i, chkb)
            answer += 1

    return answer
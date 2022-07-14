from collections import deque
def solution(n, path, order):

    tree = [[] for _ in range(n)]
    for i, j in path:
        tree[i].append(j)
        tree[j].append(i)

    orders = [0 for _ in range(n)]
    for i, j in order:
        orders[j] = i

    def bfs(x):
        visit = 0
        chkb = [False for _ in range(n)]
        after = {}
        q = deque([x])
        while q:
            ex = q.popleft()
            if orders[ex] and not chkb[orders[ex]]:
                after[orders[ex]] = ex
                continue
            visit += 1
            chkb[ex] = True
            for k in tree[ex]:
                if not chkb[k]:
                    q.append(k)

            if ex in after:
                q.append(after[ex])
        return visit

    answer = bfs(0)

    return n == answer
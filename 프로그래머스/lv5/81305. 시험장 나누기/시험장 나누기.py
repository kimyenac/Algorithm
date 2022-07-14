import sys
sys.setrecursionlimit(10**6)

l = [0] * 10005 # 왼쪽 자식 노드 번호
r = [0] * 10005 # 오른쪽 자식 노드 번호
p = [-1] * 10005 # 부모 노드 번호
x = [0] * 10005 # 시험장의 응시 인원
n = 0 # 노드의 수
root = 0 # 루트
cnt = 0 # 그룹의 수

def dfs(root, mid):
    global cnt
    lv = 0
    if l[root] != -1:
        lv = dfs(l[root], mid)
    rv = 0
    if r[root] != -1:
        rv = dfs(r[root], mid)
    if x[root] + lv + rv <= mid:
        return x[root] + lv + rv
    if x[root] + min(lv, rv) <= mid:
        cnt += 1
        return x[root] + min(lv, rv)
    cnt += 2
    return x[root]

def solve(mid):
    global cnt
    cnt = 0
    dfs(root, mid)
    cnt += 1
    return cnt

def solution(k, num, links):
    global root
    n = len(num)

    for i in range(n):
        l[i], r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1:
            p[l[i]] = i
        if r[i] != -1:
            p[r[i]] = i

    for i in range(n):
        if p[i] == -1:
            root = i
            break

    left = max(x)
    right = 10 ** 8
    while left < right:
        mid = (left+right) // 2
        if solve(mid) <= k:
            right = mid
        else:
            left = mid + 1

    return left
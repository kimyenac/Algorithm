import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
answer = 0

def dfs(x, a, tree, chkb):
    global answer
    chkb[x] = True
    for y in tree[x]:
        if not chkb[y]:
            a[x] += dfs(y, a, tree, chkb)
    answer += abs(a[x])
    return a[x]

def solution(a, edges):
    global answer
    
    if sum(a) != 0:
        return -1
    
    tree = defaultdict(list)
    chkb = [0] * len(a)
    
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
    
    dfs(0, a, tree, chkb)
    
    return answer
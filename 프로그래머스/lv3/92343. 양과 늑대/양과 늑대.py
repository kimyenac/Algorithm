import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
from copy import deepcopy
is_wolf = list()
parent = defaultdict(list)
max_sheep = 0
def dfs(start, chkb, nsheep, nwolf, can_go):
    global max_sheep
    if chkb[start]: return
    chkb[start] = True
    if is_wolf[start]:
        nwolf += 1
    else:
        nsheep += 1
        max_sheep = max(max_sheep, nsheep)
    if nwolf >= nsheep:
        return
    can_go.extend(parent[start])
    for can in can_go:
        dfs(can, deepcopy(chkb), nsheep, nwolf, can_go=[i for i in can_go if i != can and not chkb[can]])

def solution(info, edges):
    global is_wolf, parent, chkb
    is_wolf = info
    chkb = [False] * len(info)
    for a, b in edges:
        parent[a].append(b)
        
    dfs(0, chkb, 0, 0, [])
    
    return max_sheep
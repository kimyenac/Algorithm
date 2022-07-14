import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    
    preorder = []
    postorder = []
    
    def order(nodeList, levels, curLevel):
        n = nodeList[:]
        cur = n.pop(0)
        preorder.append(cur[0])
        if n:
            for i in range(len(n)):
                if n[i][1][1] == levels[curLevel+1]:
                    if n[i][1][0] < cur[1][0]:
                        order([x for x in nodeList if x[1][0] < cur[1][0]], levels, curLevel+1)
                    else:
                        order([x for x in nodeList if x[1][0] > cur[1][0]], levels, curLevel+1)
        postorder.append(cur[0])
        
    
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    nodes = sorted(list(zip(range(1, len(nodeinfo)+1), nodeinfo)), key=lambda x: (-x[1][1], x[1][0]))
    order(nodes, levels, 0)
    
    return [preorder, postorder]
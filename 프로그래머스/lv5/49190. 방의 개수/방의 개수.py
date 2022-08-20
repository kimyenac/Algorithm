from collections import deque, defaultdict
def solution(arrows):
    answer = 0
    
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)
    
    chkb = defaultdict(int)
    chkb_dict = defaultdict(int)
    
    q = deque([now])
    for i in arrows:
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            q.append(next)
            now = next
    
    now = q.popleft()
    chkb[now] = 1

    while q:
        next = q.popleft()
        if chkb[next] == 1:
            if chkb_dict[(now, next)] == 0:
                answer += 1
        else:
            chkb[next] = 1
        chkb_dict[(now, next)] = 1
        chkb_dict[(next, now)] = 1
        now = next
    
    return answer
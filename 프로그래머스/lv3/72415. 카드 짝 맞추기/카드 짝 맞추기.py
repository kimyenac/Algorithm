from itertools import permutations
from collections import defaultdict, deque
from copy import deepcopy
# 조작 횟수 카운트
def move_cost(board, start, end):
    if start == end:
        return 0
    q = deque([[start[0], start[1], 0]])
    chkb = {start}
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, c = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            ex, ey = x, y
            while True:
                ex, ey = ex+dx[k], ey+dy[k]
                if not (0<=ex<4 and 0<=ey<4):
                    ex, ey = ex-dx[k], ey-dy[k]
                    break
                elif board[ex][ey] != 0:
                    break
            if (nx, ny) == end or (ex, ey) == end: # 도착 최단 경로
                return c+1
            if (0<=nx<4 and 0<=ny<4) and (nx, ny) not in chkb:
                q.append((nx, ny, c+1))
                chkb.add((nx, ny))
            if (ex, ey) not in chkb:
                q.append((ex, ey, c+1))
                chkb.add((ex, ey))

def cls_cost(board, cdict, curr, order, cost):
    if len(order) == 0: # 모든 카드를 확인한 경우
        return cost
    idx = order[0]+1 # 현재 선택해야 할 카드의 종류

    # 현재 위치에서 A1까지의 조작 횟수 + A1-> A2까지의 조작 횟수 + 2 (카드 선택)
    choice1 = move_cost(board, curr, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(board, curr, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2: # 적은 조작 횟수를 한 경우를 따라 재귀
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)

def solution(board, r, c):
    answer = float('INF')

    # 카드 종류에 따라 좌표 저장
    cdict = defaultdict(list)
    for row in range(4):
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in permutations(range(len(cdict)), len(cdict)): # 완전탐색
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))

    return answer
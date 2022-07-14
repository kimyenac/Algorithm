def simulation(b, m, n):
    simul_set = set()
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '*':
                simul_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    for i, j in simul_set:
        b[i][j] = 0
    for idx, val in enumerate(b):
        empty = ['*'] * val.count(0)
        b[idx] = empty + [block for block in val if block != 0]
    return len(simul_set)

def solution(m, n, board):
    answer = 0
    
    board = list(map(list, zip(*board)))
    
    while True:
        simul = simulation(board, m, n)
        if simul == 0:
            return answer
        answer += simul
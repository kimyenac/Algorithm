def solution(board, moves):
    answer = 0
    board = list(map(list, zip(*board)))
    result = []
    for m in moves:
        while board[m-1] and board[m-1][0] == 0:
            board[m-1].pop(0)
        if board[m-1]:
            x = board[m-1].pop(0)
            if result and result[-1] == x:
                result.pop()
                answer += 2
            else:
                result.append(x)
    return answer
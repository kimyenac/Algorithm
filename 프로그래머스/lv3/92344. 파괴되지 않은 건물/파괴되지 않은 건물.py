def solution(board, skill):
    n = len(board)
    m = len(board[0])

    # 누적합 기록
    graph = [[0] * (m+1) for _ in range(n+1)]
    for i in skill:
        type, r1, c1, r2, c2, degree = i
        if type == 2:
            graph[r1][c1] += degree
            graph[r1][c2+1] += -degree
            graph[r2+1][c1] += -degree
            graph[r2+1][c2+1] += degree
        else:
            graph[r1][c1] += -degree
            graph[r1][c2 + 1] += degree
            graph[r2 + 1][c1] += degree
            graph[r2 + 1][c2 + 1] += -degree

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            graph[i][j+1] += graph[i][j]

    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            graph[i+1][j] += graph[i][j]

    # 배열 합치기
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += graph[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
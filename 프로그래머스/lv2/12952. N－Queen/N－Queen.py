def dfs(queen, n, row):
    cnt = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[row] == queen[i]:
                break
            if abs(queen[row] - queen[i]) == abs(row - i):
                break
        else:
            cnt += dfs(queen, n, row+1)
    return cnt

def solution(n):
    queen = [0] * n
    answer = dfs(queen, n, 0)
    
    return answer
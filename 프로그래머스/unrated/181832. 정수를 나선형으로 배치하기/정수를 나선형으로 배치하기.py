def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    right = n - 1
    left = 0
    up = 1
    down = n - 1
    
    direction = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    cnt = 1
    
    while cnt <= n * n:
        answer[i][j] = cnt
        cnt += 1
        if direction % 4 == 0 and j == right:
            right -= 1
            direction += 1
        elif direction % 4 == 1 and i == down:
            down -= 1
            direction += 1
        elif direction % 4 == 2 and j == left:
            left += 1
            direction += 1
        elif direction % 4 == 3 and i == up:
            up += 1
            direction += 1
        i += di[direction % 4]
        j += dj[direction % 4]
        
    
    return answer
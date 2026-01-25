def solution(park, routes):
    answer = []
    
    for i in range(len(park)):
        ans = []
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
            ans.append(park[i][j])
        answer.append(ans)
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        isTrue = True
        if op == 'N':
            if x - n >= 0:
                for i in range(x-n, x):
                    if park[i][y] == 'X':
                        isTrue = False
                        break
                if isTrue:
                    x -= n
        elif op == 'S':
            if x + n < len(park):
                for i in range(x, x+n+1):
                    if park[i][y] == 'X':
                        isTrue = False
                        break
                if isTrue:
                    x += n
        elif op == 'W':
            if y - n >= 0:
                for i in range(y-n, y):
                    if park[x][i] == 'X':
                        isTrue = False
                        break
                if isTrue:
                    y -= n
        else:
            if y + n < len(park[0]):
                for i in range(y, y+n+1):
                    if park[x][i] == 'X':
                        isTrue = False
                        break
                if isTrue:
                    y += n
    
    return [x, y]
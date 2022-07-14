def solution(dirs):
    answer = 0
    visited = set()
    location = {"U" : [-1, 0], "D" : [1, 0], "L" : [0, -1], "R" : [0, 1]}

    x, y = 0, 0

    for dir in dirs:
        i = location[dir]
        nx = x + i[0]
        ny = y + i[1]
        if nx > 5 or ny > 5 or nx < -5 or ny < -5:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1
        x, y = nx, ny

    return answer
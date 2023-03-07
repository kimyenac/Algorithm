def solution(dots):
    for i in range(1, len(dots)):
        x = abs(dots[0][0] - dots[i][0])
        y = abs(dots[0][1] - dots[i][1])
        if (i == 1):
            if (x / y == abs(dots[2][0] - dots[3][0]) / abs(dots[2][1] - dots[3][1])):
                return 1
        if (i == 2):
            if (x / y == abs(dots[1][0] - dots[3][0]) / abs(dots[1][1] - dots[3][1])):
                return 1
        if (i == 3):
            if (x / y == abs(dots[1][0] - dots[2][0]) / abs(dots[1][1] - dots[2][1])):
                return 1
    return 0
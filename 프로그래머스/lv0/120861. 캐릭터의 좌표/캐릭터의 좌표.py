def solution(keyinput, board):
    answer = [0, 0]
    x = board[0] // 2
    y = board[1] // 2
    for key in keyinput:
        print(answer)
        if (key == "left" and (answer[0] - 1) >= -x):
            answer[0] = answer[0] - 1
        if (key == "right" and (answer[0] + 1) <= x):
            answer[0] = answer[0] + 1
        if (key == "up" and (answer[1] + 1) <= y):
            answer[1] = answer[1] + 1
        if (key == "down" and (answer[1] - 1) >= -y):
            answer[1] = answer[1] - 1
    return answer
def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if (mode == 0):
            if (code[i] != "1" and i % 2 == 0):
                answer += code[i]
            if (code[i] == "1"):
                mode = 1
        else:
            if (code[i] != "1" and i % 2 != 0):
                answer += code[i]
            if (code[i] == "1"):
                mode = 0
    return "EMPTY" if len(answer) == 0 else answer
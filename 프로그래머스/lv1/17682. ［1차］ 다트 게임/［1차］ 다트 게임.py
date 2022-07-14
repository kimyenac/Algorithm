def solution(dartResult):
    answer = []

    dartResult = list(dartResult)

    while dartResult:
        x = dartResult.pop(0)
        if x == "S":
            answer[-1] **= 1
        elif x == "D":
            answer[-1] **= 2
        elif x == "T":
            answer[-1] **= 3
        elif x == "*":
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif x == "#":
            answer[-1] *= -1
        else:
            if x == "1" and dartResult[0] == "0":
                answer.append(10)
                dartResult.pop(0)
            else:
                answer.append(int(x))

    return sum(answer)
def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += 1
        while True:
            if (answer % 3 != 0 and "3" not in list(str(answer))):
                break;
            answer += 1
    return answer
def solution(l, r):
    answer = []
    ans = [1, 2, 3, 4, 6, 7, 8, 9]
    for i in range(l, r+1):
        if ("5" in str(i) or "0" in str(i)):
            isTrue = False
            for x in ans:
                if (str(x) in str(i)):
                    isTrue = True
                    break
            if not isTrue:
                answer.append(i)
    return [-1] if len(answer) == 0 else answer